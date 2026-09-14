[CmdletBinding()]
param(
    [int]$MaxRuns = 3,
    [int]$MaxConsecutiveFailures = 3,
    [int]$SleepSeconds = 20,
    [int]$WorkerTimeoutMinutes = 10
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$ScoutRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$Autonomous = Join-Path $ScoutRoot 'autonomous'
$CodexFallback = 'C:\Users\coler\.codex\.sandbox-bin\codex.exe'
$RemoteBranch = 'luna/k4-autonomous-scout'

function Write-Log([string]$Message) {
    $stamp = Get-Date -Format 's'
    Add-Content -LiteralPath (Join-Path $Autonomous 'supervisor.log') -Value "$stamp $Message"
}

function Get-NextSessionNumber {
    $statePath = Join-Path $Autonomous 'state.json'
    $candidate = 1
    if (Test-Path -LiteralPath $statePath -PathType Leaf) {
        try {
            $state = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
            $candidate = [Math]::Max(1, ([int]$state.iteration) + 1)
        } catch {
            Write-Log "STATE read warning: $($_.Exception.Message)"
        }
    }
    while ((Test-Path -LiteralPath (Join-Path $Autonomous ("session-{0:D2}-final.md" -f $candidate))) -or
           (Test-Path -LiteralPath (Join-Path $Autonomous ("session-{0:D2}-output.log" -f $candidate)))) {
        $candidate++
    }
    return $candidate
}

function Get-DescendantIds([int]$RootPid) {
    $all = @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue)
    $seen = New-Object 'System.Collections.Generic.HashSet[int]'
    $queue = New-Object 'System.Collections.Generic.Queue[int]'
    [void]$queue.Enqueue($RootPid)
    $children = @()
    while ($queue.Count -gt 0) {
        $parentPid = $queue.Dequeue()
        foreach ($proc in ($all | Where-Object { $_.ParentProcessId -eq $parentPid })) {
            if ($seen.Add([int]$proc.ProcessId)) {
                $children += [int]$proc.ProcessId
                [void]$queue.Enqueue([int]$proc.ProcessId)
            }
        }
    }
    return $children
}

function Stop-ProcessTree([int]$RootPid) {
    $descendants = @(Get-DescendantIds -RootPid $RootPid)
    foreach ($childPid in ($descendants | Sort-Object -Descending)) {
        Stop-Process -Id $childPid -Force -ErrorAction SilentlyContinue
    }
    Stop-Process -Id $RootPid -Force -ErrorAction SilentlyContinue
    Start-Sleep -Milliseconds 500
    $remaining = @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue | Where-Object {
        $_.ProcessId -eq $RootPid -or $descendants -contains [int]$_.ProcessId
    })
    return $remaining
}

function Drain-ReadTask {
    param(
        [Parameter(Mandatory=$true)][ref]$Task,
        [Parameter(Mandatory=$true)][ref]$Open,
        [Parameter(Mandatory=$true)][System.IO.StreamWriter]$Writer,
        [Parameter(Mandatory=$true)][System.IO.StreamReader]$Reader,
        [string]$Label
    )
    if (-not $Open.Value -or -not $Task.Value.IsCompleted) { return }
    try {
        $line = $Task.Value.Result
    } catch {
        $line = "[$Label stream error: $($_.Exception.Message)]"
    }
    if ($null -eq $line) {
        $Open.Value = $false
    } else {
        $Writer.WriteLine($line)
        $Writer.Flush()
        $Task.Value = $Reader.ReadLineAsync()
    }
}

function Quote-ProcessArgument([string]$Value) {
    if ($Value -notmatch '[\s"]') { return $Value }
    $escaped = $Value -replace '(\\*)"', '$1$1\"'
    $escaped = $escaped -replace '(\\+)$', '$1$1'
    return '"' + $escaped + '"'
}

if (-not (Test-Path -LiteralPath $Autonomous -PathType Container)) {
    New-Item -ItemType Directory -Path $Autonomous -Force | Out-Null
}

$cmd = Get-Command codex -ErrorAction SilentlyContinue
if ($null -ne $cmd) { $Codex = $cmd.Source } elseif (Test-Path -LiteralPath $CodexFallback) { $Codex = $CodexFallback } else {
    throw 'codex.exe was not found via PATH or the verified fallback path.'
}

$isRepo = (& git -C $ScoutRoot rev-parse --is-inside-work-tree 2>$null)
if ($isRepo -ne 'true') { throw "Scout path is not a Git worktree: $ScoutRoot" }
$branch = (& git -C $ScoutRoot branch --show-current).Trim()
if ($branch -ne $RemoteBranch) { throw "Refusing to run on branch '$branch'; expected '$RemoteBranch'." }
if ($branch -eq 'main' -or $branch -eq 'codex/k4-continuation' -or $branch -like 'claude/*') {
    throw "Protected branch guard rejected '$branch'."
}

$GitCommonDir = (& git -C $ScoutRoot rev-parse --path-format=absolute --git-common-dir).Trim()
if (-not (Test-Path -LiteralPath $GitCommonDir -PathType Container)) { throw "Git common directory is unavailable: $GitCommonDir" }
$sessionNumber = Get-NextSessionNumber
$timeoutSeconds = [Math]::Max(1, $WorkerTimeoutMinutes * 60)
Write-Log "START branch=$branch root=$ScoutRoot model=gpt-5.6-luna maxRuns=$MaxRuns timeoutSeconds=$timeoutSeconds sessionStart=$sessionNumber mcp=disabled"
$SafeWorkerRoot = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $GitCommonDir))
if (-not (Test-Path -LiteralPath $SafeWorkerRoot -PathType Container)) { throw "Safe worker root is unavailable: $SafeWorkerRoot" }

$failures = 0
$run = 0
while ($run -lt $MaxRuns) {
    if (Test-Path -LiteralPath (Join-Path $Autonomous 'STOP') -PathType Leaf) {
        Write-Log 'STOP marker found; exiting cleanly.'
        break
    }
    if (Test-Path -LiteralPath (Join-Path $Autonomous 'STOP_FOR_SOL') -PathType Leaf) {
        Write-Log 'STOP_FOR_SOL marker found; exiting for supervisor review.'
        break
    }

    $run++
    $session = $sessionNumber + $run - 1
    $tag = '{0:D2}' -f $session
    $finalPath = Join-Path $Autonomous "session-$tag-final.md"
    $outputPath = Join-Path $Autonomous "session-$tag-output.log"
    $continuation = @"
This is bounded scout iteration $session of at most $MaxRuns for this supervisor invocation. Read
AUTONOMOUS_SCOUT.md first and consult autonomous/state.json and autonomous/research-ledger.md.
Perform exactly ONE highest-information task, then update state/ledger as appropriate and exit.
Do not launch EXP-040 or any large search. Work only on branch luna/k4-autonomous-scout. If you
discover an escalation finding, create ESCALATE_TO_SOL.md and autonomous/STOP_FOR_SOL, then stop.
Save a compact final report.
"@
    $continuation = "The scout worktree is '$ScoutRoot'. Use absolute paths or git -C '$ScoutRoot' for all research files and Git operations. Do not edit the launcher workspace or any other worktree.`r`n`r`n" + $continuation
    Write-Log "RUN $session begin"
    $process = $null
    $writer = $null
    try {
        $prompt = Get-Content -LiteralPath (Join-Path $ScoutRoot 'AUTONOMOUS_SCOUT.md') -Raw
        $prompt = $prompt + "`r`n`r`n" + $continuation
        $arguments = @(
            '--search', 'exec',
            '-c', 'approval_policy="never"',
            '-c', 'sandbox_workspace_write.network_access=true',
            '-c', 'sandbox_mode="workspace-write"',
            '-c', 'mcp_servers.blender.enabled=false',
            '-c', 'mcp_servers.codex-imagen.enabled=false',
            '-c', 'mcp_servers.node_repl.enabled=false',
            '-c', 'mcp_servers.unityMCP.enabled=false',
            '-c', 'mcp_servers.cua_repl={command="C:\\\\Users\\\\coler\\\\AppData\\\\Local\\\\OpenAI\\\\Codex\\\\runtimes\\\\cua_node\\\\a708e72b10c27b59\\\\bin\\\\node.exe",args=["C:\\\\Users\\\\coler\\\\AppData\\\\Local\\\\OpenAI\\\\Codex\\\\runtimes\\\\cua_node\\\\a708e72b10c27b59\\\\bin\\\\node_modules\\\\@oai\\\\cua-repl\\\\bin\\\\cua-repl.mjs"],enabled=false}',
            '--model', 'gpt-5.6-luna', '--sandbox', 'workspace-write',
            '--add-dir', $ScoutRoot,
            '--add-dir', $GitCommonDir,
            '--cd', $SafeWorkerRoot, '--skip-git-repo-check', '-o', $finalPath, '-'
        )
        $psi = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName = $Codex
        $psi.WorkingDirectory = $SafeWorkerRoot
        $psi.UseShellExecute = $false
        $psi.CreateNoWindow = $true
        $psi.RedirectStandardInput = $true
        $psi.RedirectStandardOutput = $true
        $psi.RedirectStandardError = $true
        if ($psi.PSObject.Properties.Name -contains 'ArgumentList') {
            foreach ($arg in $arguments) { [void]$psi.ArgumentList.Add([string]$arg) }
        } else {
            $psi.Arguments = (($arguments | ForEach-Object { Quote-ProcessArgument ([string]$_) }) -join ' ')
        }
        $process = New-Object System.Diagnostics.Process
        $process.StartInfo = $psi
        $writer = [System.IO.File]::CreateText($outputPath)
        if (-not $process.Start()) { throw 'Codex process failed to start.' }
        $process.StandardInput.Write($prompt)
        $process.StandardInput.Close()
        $stdoutOpen = $true
        $stderrOpen = $true
        $stdoutTask = $process.StandardOutput.ReadLineAsync()
        $stderrTask = $process.StandardError.ReadLineAsync()
        $deadline = [DateTime]::UtcNow.AddSeconds($timeoutSeconds)
        while (-not $process.HasExited -and [DateTime]::UtcNow -lt $deadline) {
            Drain-ReadTask ([ref]$stdoutTask) ([ref]$stdoutOpen) $writer $process.StandardOutput 'stdout'
            Drain-ReadTask ([ref]$stderrTask) ([ref]$stderrOpen) $writer $process.StandardError 'stderr'
            Start-Sleep -Milliseconds 100
        }
        if (-not $process.HasExited) {
            $workerPid = $process.Id
            $remaining = @(Stop-ProcessTree -RootPid $workerPid)
            Write-Log "RUN $session TIMEOUT pid=$workerPid timeoutSeconds=$timeoutSeconds remainingProcesses=$($remaining.Count)"
            throw "Codex worker exceeded $timeoutSeconds seconds."
        }
        $drainDeadline = [DateTime]::UtcNow.AddSeconds(5)
        while (($stdoutOpen -or $stderrOpen) -and [DateTime]::UtcNow -lt $drainDeadline) {
            Drain-ReadTask ([ref]$stdoutTask) ([ref]$stdoutOpen) $writer $process.StandardOutput 'stdout'
            Drain-ReadTask ([ref]$stderrTask) ([ref]$stderrOpen) $writer $process.StandardError 'stderr'
            Start-Sleep -Milliseconds 25
        }
        $process.WaitForExit()
        $exitCode = $process.ExitCode
        Write-Log "RUN $session exit=$exitCode"
        if ($exitCode -eq 0 -and (Test-Path -LiteralPath $finalPath -PathType Leaf)) {
            $finalText = Get-Content -LiteralPath $finalPath -Raw
            if ($finalText -match '(?im)^\s*(?:Iteration .*\bblocked\b|Classification:.*\bBLOCKED\b)') { throw 'Worker reported a blocked iteration.' }
        }
        if ($exitCode -ne 0) { throw "Codex exited with status $exitCode" }
        $failures = 0
        Write-Log "RUN $session success final=$finalPath"
        & git -C $ScoutRoot push origin $RemoteBranch 2>&1 | Add-Content -LiteralPath (Join-Path $Autonomous 'supervisor.log')
        if ($LASTEXITCODE -ne 0) { throw "git push exited with status $LASTEXITCODE" }
        Write-Log "RUN $session push success"
    } catch {
        $failures++
        Write-Log "RUN $session failure count=$failures error=$($_.Exception.Message)"
        if ($failures -ge $MaxConsecutiveFailures) {
            Write-Log 'Repeated failure limit reached; exiting.'
            break
        }
    } finally {
        if ($null -ne $writer) { $writer.Dispose() }
        if ($null -ne $process) { $process.Dispose() }
    }
    if ($run -lt $MaxRuns -and $SleepSeconds -gt 0) { Start-Sleep -Seconds $SleepSeconds }
}
Write-Log "END runs=$run failures=$failures"
