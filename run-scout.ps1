[CmdletBinding()]
param(
    [int]$MaxRuns = 12,
    [int]$MaxConsecutiveFailures = 3,
    [int]$SleepSeconds = 20,
    [int]$WorkerTimeoutMinutes = 10,
    [int]$SolTimeoutMinutes = 5,
    [switch]$ValidationOnly,
    [switch]$SkipValidation
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$Autonomous = Join-Path $Root 'autonomous'
$RemoteBranch = 'luna/k4-autonomous-scout'
$LauncherRoot = 'C:\Users\coler\Documents\Codex\2026-09-11\referenced-chatgpt-conversation-this-is-an'
$CodexFallback = 'C:\Users\coler\.codex\.sandbox-bin\codex.exe'
$LunaModel = 'gpt-5.6-luna'
$LunaEffort = 'xhigh'
$SolModel = 'gpt-5.6-sol'
$SolEffort = 'low'
$PidPath = Join-Path $Autonomous 'supervisor.pid'

function Write-Log([string]$Message) {
    $stamp = (Get-Date).ToUniversalTime().ToString('s') + 'Z'
    Add-Content -LiteralPath (Join-Path $Autonomous 'supervisor.log') -Value "$stamp $Message"
}

function Get-NextSessionNumber {
    $statePath = Join-Path $Autonomous 'state.json'
    $candidate = 1
    if (Test-Path -LiteralPath $statePath -PathType Leaf) {
        try {
            $state = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
            $candidate = [Math]::Max(1, ([int]$state.iteration) + 1)
        } catch { Write-Log "STATE read warning: $($_.Exception.Message)" }
    }
    while ((Test-Path -LiteralPath (Join-Path $Autonomous ("session-{0:D4}-luna-final.md" -f $candidate))) -or
           (Test-Path -LiteralPath (Join-Path $Autonomous ("session-{0:D4}-luna-output.log" -f $candidate)))) { $candidate++ }
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
    return @(Get-CimInstance Win32_Process -ErrorAction SilentlyContinue | Where-Object {
        $_.ProcessId -eq $RootPid -or $descendants -contains [int]$_.ProcessId
    })
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
    try { $line = $Task.Value.Result } catch { $line = "[$Label stream error: $($_.Exception.Message)]" }
    if ($null -eq $line) { $Open.Value = $false }
    else { $Writer.WriteLine($line); $Writer.Flush(); $Task.Value = $Reader.ReadLineAsync() }
}

function Quote-ProcessArgument([string]$Value) {
    if ($Value -notmatch '[\s"]') { return $Value }
    $escaped = $Value -replace '(\\*)"', '$1$1\"'
    $escaped = $escaped -replace '(\\+)$', '$1$1'
    return '"' + $escaped + '"'
}

function Invoke-CodexWorker {
    param(
        [Parameter(Mandatory=$true)][string]$Role,
        [Parameter(Mandatory=$true)][string]$Model,
        [Parameter(Mandatory=$true)][string]$Effort,
        [Parameter(Mandatory=$true)][int]$TimeoutSeconds,
        [Parameter(Mandatory=$true)][string]$Prompt,
        [Parameter(Mandatory=$true)][string]$FinalPath,
        [Parameter(Mandatory=$true)][string]$OutputPath
    )
    $arguments = @(
        '--search', 'exec',
        '-c', 'approval_policy="never"',
        '-c', 'sandbox_workspace_write.network_access=true',
        '-c', 'sandbox_mode="workspace-write"',
        '-c', ('model_reasoning_effort="' + $Effort + '"'),
        '-c', 'mcp_servers.blender.enabled=false',
        '-c', 'mcp_servers.codex-imagen.enabled=false',
        '-c', 'mcp_servers.node_repl.enabled=false',
        '-c', 'mcp_servers.unityMCP.enabled=false',
        '-c', 'mcp_servers.cua_repl={command="C:\\\\Users\\\\coler\\\\AppData\\\\Local\\\\OpenAI\\\\Codex\\\\runtimes\\\\cua_node\\\\a708e72b10c27b59\\\\bin\\\\node.exe",args=["C:\\\\Users\\\\coler\\\\AppData\\\\Local\\\\OpenAI\\\\Codex\\\\runtimes\\\\cua_node\\\\a708e72b10c27b59\\\\bin\\\\node_modules\\\\@oai\\\\cua-repl\\\\bin\\\\cua-repl.mjs"],enabled=false}',
        '--model', $Model, '--sandbox', 'workspace-write', '--add-dir', $Root,
        '--cd', $LauncherRoot, '--skip-git-repo-check', '-o', $FinalPath, '-'
    )
    $psi = New-Object System.Diagnostics.ProcessStartInfo
    $psi.FileName = $Codex
    $psi.WorkingDirectory = $LauncherRoot
    $psi.UseShellExecute = $false
    $psi.CreateNoWindow = $true
    $psi.RedirectStandardInput = $true
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    if ($psi.PSObject.Properties.Name -contains 'ArgumentList') {
        foreach ($arg in $arguments) { [void]$psi.ArgumentList.Add([string]$arg) }
    } else { $psi.Arguments = (($arguments | ForEach-Object { Quote-ProcessArgument ([string]$_) }) -join ' ') }
    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $psi
    $writer = [System.IO.File]::CreateText($OutputPath)
    try {
        if (-not $process.Start()) { throw "$Role Codex process failed to start." }
        $process.StandardInput.Write($Prompt)
        $process.StandardInput.Close()
        $stdoutOpen = $true; $stderrOpen = $true
        $stdoutTask = $process.StandardOutput.ReadLineAsync()
        $stderrTask = $process.StandardError.ReadLineAsync()
        $deadline = [DateTime]::UtcNow.AddSeconds($TimeoutSeconds)
        while (-not $process.HasExited -and [DateTime]::UtcNow -lt $deadline) {
            Drain-ReadTask ([ref]$stdoutTask) ([ref]$stdoutOpen) $writer $process.StandardOutput 'stdout'
            Drain-ReadTask ([ref]$stderrTask) ([ref]$stderrOpen) $writer $process.StandardError 'stderr'
            Start-Sleep -Milliseconds 100
        }
        if (-not $process.HasExited) {
            $workerPid = $process.Id
            $remaining = @(Stop-ProcessTree -RootPid $workerPid)
            Write-Log "$Role TIMEOUT pid=$workerPid timeoutSeconds=$TimeoutSeconds remainingProcesses=$($remaining.Count)"
            return [pscustomobject]@{ ExitCode = $null; TimedOut = $true; Blocked = $false }
        }
        $drainDeadline = [DateTime]::UtcNow.AddSeconds(5)
        while (($stdoutOpen -or $stderrOpen) -and [DateTime]::UtcNow -lt $drainDeadline) {
            Drain-ReadTask ([ref]$stdoutTask) ([ref]$stdoutOpen) $writer $process.StandardOutput 'stdout'
            Drain-ReadTask ([ref]$stderrTask) ([ref]$stderrOpen) $writer $process.StandardError 'stderr'
            Start-Sleep -Milliseconds 25
        }
        $process.WaitForExit()
        return [pscustomobject]@{ ExitCode = $process.ExitCode; TimedOut = $false; Blocked = $false }
    } finally {
        $writer.Dispose()
        $process.Dispose()
    }
}

function Get-Classification([string]$Path) {
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) { return 'BLOCKED' }
    $text = Get-Content -LiteralPath $Path -Raw
    $m = [regex]::Match($text, '(?im)^\s*Classification:\s*([A-Z_]+)')
    if ($m.Success) { return $m.Groups[1].Value.ToUpperInvariant() }
    if ($text -match '(?im)\bblocked\b') { return 'BLOCKED' }
    return 'LOW_VALUE'
}

function Update-State {
    param([int]$Session,[string]$Lane,[string]$Task,[string]$Result,[bool]$Useful)
    $statePath = Join-Path $Autonomous 'state.json'
    $state = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
    $state.iteration = ([int]$state.iteration) + 1
    $state.last_lane = $Lane
    $state.last_task = $Task
    $state.last_result = $Result
    $state.consecutive_no_new_findings = if ($Useful) { 0 } else { ([int]$state.consecutive_no_new_findings) + 1 }
    $state.last_commit = (& git -C $Root rev-parse HEAD).Trim()
    $state.last_updated = (Get-Date).ToString('o')
    $recent = @($state.recent_tasks) + @("$Session`: $Lane - $Task")
    if ($recent.Count -gt 12) { $recent = $recent[($recent.Count-12)..($recent.Count-1)] }
    $state.recent_tasks = @($recent)
    ($state | ConvertTo-Json -Depth 5) | Set-Content -LiteralPath $statePath -Encoding UTF8
}

function Commit-And-Push([string]$Message) {
    $current = (& git -C $Root branch --show-current).Trim()
    if ($current -ne $RemoteBranch) { throw "Refusing push from branch '$current'." }
    & git -C $Root add autonomous
    if ((& git -C $Root status --porcelain)) {
        & git -C $Root commit -m $Message 2>&1 | Add-Content -LiteralPath (Join-Path $Autonomous 'supervisor.log')
        if ($LASTEXITCODE -ne 0) { throw "git commit failed ($LASTEXITCODE)." }
    }
    & git -C $Root push origin $RemoteBranch 2>&1 | Add-Content -LiteralPath (Join-Path $Autonomous 'supervisor.log')
    if ($LASTEXITCODE -ne 0) { throw "git push failed ($LASTEXITCODE)." }
}

if (-not (Test-Path -LiteralPath $Autonomous -PathType Container)) { New-Item -ItemType Directory -Path $Autonomous -Force | Out-Null }
$cmd = Get-Command codex -ErrorAction SilentlyContinue
if ($null -ne $cmd) { $Codex = $cmd.Source } elseif (Test-Path -LiteralPath $CodexFallback) { $Codex = $CodexFallback } else { throw 'codex.exe not found.' }
$isRepo = (& git -C $Root rev-parse --is-inside-work-tree 2>$null).Trim()
if ($isRepo -ne 'true') { throw "Not a Git repository: $Root" }
$branch = (& git -C $Root branch --show-current).Trim()
if ($branch -ne $RemoteBranch -or $branch -eq 'main' -or $branch -eq 'codex/k4-continuation' -or $branch -like 'claude/*') { throw "Protected/incorrect branch: $branch" }
$script:Codex = $Codex

$keepAwakeEnabled = $false
$ES_CONTINUOUS = [uint32]2147483648
$ES_SYSTEM_REQUIRED = [uint32]1
try {
    Add-Type @'
using System;
using System.Runtime.InteropServices;
public static class K4KeepAwake {
    [DllImport("kernel32.dll")] public static extern uint SetThreadExecutionState(uint flags);
}
'@ -ErrorAction Stop
    [void][K4KeepAwake]::SetThreadExecutionState($ES_CONTINUOUS -bor $ES_SYSTEM_REQUIRED)
    $keepAwakeEnabled = $true
    Write-Log 'KEEP_AWAKE enabled (thread-scoped).'
} catch { Write-Log "KEEP_AWAKE unavailable: $($_.Exception.Message)" }

try {
    Set-Content -LiteralPath $PidPath -Value ([string]$PID) -Encoding ASCII
    $sessionNumber = Get-NextSessionNumber
    Write-Log "START branch=$branch root=$Root model=$LunaModel effort=$LunaEffort sol=$SolModel solEffort=$SolEffort maxRuns=$MaxRuns lunaTimeoutSeconds=$($WorkerTimeoutMinutes*60) solTimeoutSeconds=$($SolTimeoutMinutes*60) sessionStart=$sessionNumber"
    if (-not $SkipValidation) {
        $stamp = (Get-Date).ToUniversalTime().ToString('yyyyMMdd-HHmmss')
        $validationFinal = Join-Path $Autonomous "validation-$stamp-luna-final.md"
        $validationOutput = Join-Path $Autonomous "validation-$stamp-luna-output.log"
        $validationPrompt = @"
Startup validation only. Read AUTONOMOUS_SCOUT.md, autonomous/KNOWN_STATE.md, autonomous/state.json,
autonomous/research-ledger.md, and autonomous/open-questions.md from this standalone repository.
Do not research or modify canonical files. Perform exactly these cheap checks: git status, git log,
rg --files, read one line from KNOWN_STATE, create then remove autonomous/.validation-luna.tmp,
and perform one harmless public web search for official Kryptos documentation. Confirm the active
branch is luna/k4-autonomous-scout, model is $LunaModel, and your requested reasoning effort is
$LunaEffort. Final line must be `VALIDATION: PASS` only if every check succeeds; otherwise
`VALIDATION: FAIL` with the blocking reason.
"@
        $vr = Invoke-CodexWorker -Role 'LUNA_VALIDATION' -Model $LunaModel -Effort $LunaEffort -TimeoutSeconds 180 -Prompt $validationPrompt -FinalPath $validationFinal -OutputPath $validationOutput
        $validationText = if(Test-Path -LiteralPath $validationFinal){Get-Content $validationFinal -Raw}else{''}
        if ($vr.TimedOut -or $vr.ExitCode -ne 0 -or $validationText -notmatch '(?im)VALIDATION:\s*PASS') {
            $reason = if($vr.TimedOut){'Luna validation timeout'}elseif($vr.ExitCode -ne 0){"Luna validation exit $($vr.ExitCode)"}else{'Luna validation did not report PASS'}
            Set-Content -LiteralPath (Join-Path $Autonomous 'STARTUP_FAILURE.md') -Value "# Startup failure`r`n`r`n$reason`r`n`r`nSee $validationOutput and $validationFinal." -Encoding UTF8
            Write-Log "VALIDATION FAILURE: $reason"
            throw $reason
        }
        $solFinal = Join-Path $Autonomous "validation-$stamp-sol-review.md"
        $solOutput = Join-Path $Autonomous "validation-$stamp-sol-output.log"
        $solPrompt = @"
You are GPT-5.6 Sol at LOW for a tiny startup review. Read autonomous/KNOWN_STATE.md and verify
the standalone repository branch with git status/log. Review the following Luna validation report:
---
$validationText
---
Check only whether the validation is credible, whether MCP startup errors are absent, and whether
the worker configuration names gpt-5.6-luna at xhigh and gpt-5.6-sol at low. Do not research K4.
Final lines must be `SOL_VALIDATION: PASS` if credible or `SOL_VALIDATION: FAIL` with a reason.
"@
        $sr = Invoke-CodexWorker -Role 'SOL_VALIDATION' -Model $SolModel -Effort $SolEffort -TimeoutSeconds 120 -Prompt $solPrompt -FinalPath $solFinal -OutputPath $solOutput
        $solText = if(Test-Path -LiteralPath $solFinal){Get-Content $solFinal -Raw}else{''}
        if ($sr.TimedOut -or $sr.ExitCode -ne 0 -or $solText -notmatch '(?im)SOL_VALIDATION:\s*PASS') {
            $reason = if($sr.TimedOut){'Sol validation timeout'}elseif($sr.ExitCode -ne 0){"Sol validation exit $($sr.ExitCode)"}else{'Sol validation did not report PASS'}
            Set-Content -LiteralPath (Join-Path $Autonomous 'STARTUP_FAILURE.md') -Value "# Startup failure`r`n`r`n$reason`r`n`r`nSee $solOutput and $solFinal." -Encoding UTF8
            Write-Log "VALIDATION FAILURE: $reason"
            throw $reason
        }
        Write-Log 'VALIDATION PASS Luna+Sol; entering research loop.'
        if ($ValidationOnly) { return }
    }
    if ($ValidationOnly) { return }
    $failures = 0
    $run = 0
    while ($run -lt $MaxRuns) {
        if (Test-Path -LiteralPath (Join-Path $Autonomous 'STOP') -PathType Leaf) { Write-Log 'STOP marker found; exiting.'; break }
        if (Test-Path -LiteralPath (Join-Path $Autonomous 'STOP_FOR_SOL') -PathType Leaf) { Write-Log 'STOP_FOR_SOL marker found; exiting.'; break }
        $run++
        $session = $sessionNumber + $run - 1
        $tag = '{0:D4}' -f $session
        $lunaFinal = Join-Path $Autonomous "session-$tag-luna-final.md"
        $lunaOutput = Join-Path $Autonomous "session-$tag-luna-output.log"
        $continuation = @"
This is bounded Luna iteration $session of at most $MaxRuns. Read AUTONOMOUS_SCOUT.md, KNOWN_STATE.md,
state.json, research-ledger.md, and open-questions.md before choosing one task. Use only the standalone
repository at $Root and branch $RemoteBranch. Do exactly one bounded investigation, check novelty,
record a compact report with one allowed Classification line, and commit useful scoped changes.
Do not launch EXP-040, brute-force, language-score, or create another Codex process. If a candidate
could materially change the frontier, stop and create ESCALATE_TO_SOL.md plus autonomous/STOP_FOR_SOL.
No solution material is allowed. Current no-result count is read from state; change lane after four.
"@
        Write-Log "RUN $session begin"
        try {
            $p = Get-Content -LiteralPath (Join-Path $Root 'AUTONOMOUS_SCOUT.md') -Raw
            $lr = Invoke-CodexWorker -Role "LUNA_$session" -Model $LunaModel -Effort $LunaEffort -TimeoutSeconds ($WorkerTimeoutMinutes*60) -Prompt ($p+"`r`n`r`n"+$continuation) -FinalPath $lunaFinal -OutputPath $lunaOutput
            if ($lr.TimedOut) { throw 'Luna timeout.' }
            if ($lr.ExitCode -ne 0) { throw "Luna exit $($lr.ExitCode)." }
            $classification = Get-Classification -Path $lunaFinal
            Write-Log "RUN $session Luna classification=$classification exit=0"
            $solRecommendation = 'NONE'
            if ($classification -in @('NEW_CANDIDATE','CONTRADICTION_CANDIDATE','IDEA_CANDIDATE')) {
                $solFinal = Join-Path $Autonomous "session-$tag-sol-review.md"
                $solOutput = Join-Path $Autonomous "session-$tag-sol-output.log"
                $candidate = Get-Content -LiteralPath $lunaFinal -Raw
                $sp = @"
You are GPT-5.6 Sol at LOW, a skeptical reviewer. Read autonomous/KNOWN_STATE.md and search the
repository before accepting anything. Review this Luna report only; do not do broad research:
---
$candidate
---
Return exactly these fields:
NOVELTY: VALID | ALREADY_KNOWN | UNCERTAIN
EVIDENCE: STRONG | MEDIUM | WEAK | SPECULATIVE
CHECKPOINT_IMPACT: NONE | MINOR | MATERIAL | FRONTIER_CHANGING
RECOMMENDATION: REJECT | RECORD | FOLLOW_UP | ESCALATE
SHORT_REASON: one concise reason
"@
                $sr = Invoke-CodexWorker -Role "SOL_$session" -Model $SolModel -Effort $SolEffort -TimeoutSeconds ($SolTimeoutMinutes*60) -Prompt $sp -FinalPath $solFinal -OutputPath $solOutput
                if ($sr.TimedOut) { throw 'Sol timeout.' }
                if ($sr.ExitCode -ne 0) { throw "Sol exit $($sr.ExitCode)." }
                $solText = Get-Content -LiteralPath $solFinal -Raw
                $m = [regex]::Match($solText,'(?im)^RECOMMENDATION:\s*(\S+)'); if($m.Success){$solRecommendation=$m.Groups[1].Value.ToUpperInvariant()}
                Write-Log "RUN $session Sol recommendation=$solRecommendation"
                if ($solRecommendation -eq 'ESCALATE' -or $solText -match '(?im)CHECKPOINT_IMPACT:\s*(MATERIAL|FRONTIER_CHANGING)') {
                    $esc = "# Escalation to stronger Sol review`r`n`r`nSession: $session`r`n`r`n$(Get-Content $solFinal -Raw)`r`n`r`nLuna report: $lunaFinal"
                    Set-Content -LiteralPath (Join-Path $Root 'ESCALATE_TO_SOL.md') -Value $esc -Encoding UTF8
                    New-Item -ItemType File -Path (Join-Path $Autonomous 'STOP_FOR_SOL') -Force | Out-Null
                    Write-Log "RUN $session escalation marker created; stopping loop."
                }
            }
            $useful = $classification -in @('NEW_CANDIDATE','CONTRADICTION_CANDIDATE','CONFIRMATION') -and $solRecommendation -notin @('REJECT','NONE')
            $task = if($classification -eq 'BLOCKED'){'worker blocked'}else{'bounded lane task'}
            Update-State -Session $session -Lane 'AUTO' -Task $task -Result "$classification/$solRecommendation" -Useful $useful
            Add-Content -LiteralPath (Join-Path $Autonomous 'session-log.md') -Value "`r`n### Session $session`r`n- Luna: $classification`r`n- Sol: $solRecommendation`r`n- Final: $lunaFinal"
            Commit-And-Push "Luna/Sol scout: record session $session"
            $failures = 0
            Write-Log "RUN $session success push=ok"
        } catch {
            $failures++
            Write-Log "RUN $session failure count=$failures error=$($_.Exception.Message)"
            if ($failures -ge $MaxConsecutiveFailures) { Write-Log 'Repeated failure limit reached; exiting.'; break }
        }
        if (Test-Path -LiteralPath (Join-Path $Autonomous 'STOP_FOR_SOL') -PathType Leaf) { break }
        if ($run -lt $MaxRuns -and $SleepSeconds -gt 0) { Start-Sleep -Seconds $SleepSeconds }
    }
    Write-Log "END runs=$run failures=$failures"
} finally {
    try { if ($keepAwakeEnabled) { [void][K4KeepAwake]::SetThreadExecutionState($ES_CONTINUOUS) } } catch {}
    if (Test-Path -LiteralPath $PidPath) { Remove-Item -LiteralPath $PidPath -Force -ErrorAction SilentlyContinue }
    Write-Log 'KEEP_AWAKE restored; supervisor exited.'
}
