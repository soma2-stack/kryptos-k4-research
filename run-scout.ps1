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
        $parent = $queue.Dequeue()
        foreach ($proc in ($all | Where-Object { $_.ParentProcessId -eq $parent })) {
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
    foreach ($pid in ($descendants | Sort-Object -Descending)) {
        Stop-Process -Id $pid -Force -ErrorAction SilentlyContinue
    }
    Stop-Process -Id $RootPid -Force -ErrorAction SilentlyContinue
    Start-Sleep -Milliseconds 500
    $remaining = @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue | Where-Object {
        $_.ProcessId -eq $RootPid -or $descendants -contains [int]$_.ProcessId
    })
    return $remaining
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

$sessionNumber = Get-NextSessionNumber
$timeoutSeconds = [Math]::Max(1, $WorkerTimeoutMinutes * 60)
Write-Log "START branch=$branch root=$ScoutRoot model=gpt-5.6-luna maxRuns=$MaxRuns timeoutSeconds=$timeoutSeconds sessionStart=$sessionNumber"

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
    Write-Log "RUN $session begin"
    $process = $null
    $writer = $null
    try {
        $prompt = Get-Content -LiteralPath (Join-Path $ScoutRoot 'AUTONOMOUS_SCOUT.md') -Raw
        $prompt = $prompt + "`r`n`r`n" + $continuation
        $arguments = @(
            '-c', 'approval_policy="never"',
            '-c', 'sandbox_workspace_write.network_access=true',
            '-c', 'mcp_servers.blender.enabled=false',
            '-c', 'mcp_servers.codex-imagen.enabled=false',
            '-c', 'mcp_servers.codex_app.enabled=false',
            '-c', 'mcp_servers.cua_repl.enabled=false',
            '-c', 'mcp_servers.node_repl.enabled=false',
            '-c', 'mcp_servers.unityMCP.enabled=false',
            '--search', 'exec', '--model', 'gpt-5.6-luna', '--sandbox', 'workspace-write',
            '-C', $ScoutRoot, '-o', $finalPath, '-'
        )
        $psi = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName = $Codex
        $psi.WorkingDirectory = $ScoutRoot
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
        $handler = [System.Diagnostics.DataReceivedEventHandler]{
            param($sender, $event)
            if ($null -ne $event.Data) { $writer.WriteLine($event.Data); $writer.Flush() }
        }
        [void]$process.add_OutputDataReceived($handler)
        [void]$process.add_ErrorDataReceived($handler)
        if (-not $process.Start()) { throw 'Codex process failed to start.' }
        $process.BeginOutputReadLine()
        $process.BeginErrorReadLine()
        $process.StandardInput.Write($prompt)
        $process.StandardInput.Close()
        $deadline = [DateTime]::UtcNow.AddSeconds($timeoutSeconds)
        while (-not $process.HasExited -and [DateTime]::UtcNow -lt $deadline) {
            Start-Sleep -Milliseconds 500
        }
        if (-not $process.HasExited) {
            $pid = $process.Id
            $remaining = @(Stop-ProcessTree -RootPid $pid)
            Write-Log "RUN $session TIMEOUT pid=$pid timeoutSeconds=$timeoutSeconds remainingProcesses=$($remaining.Count)"
            throw "Codex worker exceeded $timeoutSeconds seconds."
        }
        $process.WaitForExit()
        $exitCode = $process.ExitCode
        Write-Log "RUN $session exit=$exitCode"
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
