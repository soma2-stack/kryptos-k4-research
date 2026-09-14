[CmdletBinding()]
param(
    [int]$MaxRuns = 12,
    [int]$MaxConsecutiveFailures = 3,
    [int]$SleepSeconds = 20
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
Write-Log "START branch=$branch root=$ScoutRoot model=gpt-5.6-luna maxRuns=$MaxRuns"

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
    $tag = '{0:D2}' -f $run
    $finalPath = Join-Path $Autonomous "session-$tag-final.md"
    $outputPath = Join-Path $Autonomous "session-$tag-output.log"
    $continuation = @"
This is bounded scout iteration $run of at most $MaxRuns. Read AUTONOMOUS_SCOUT.md first and
consult autonomous/state.json and autonomous/research-ledger.md. Perform exactly ONE highest-
information task, then update state/ledger as appropriate and exit. Do not launch EXP-040 or any
large search. Work only on branch luna/k4-autonomous-scout. If you discover an escalation finding,
create ESCALATE_TO_SOL.md and autonomous/STOP_FOR_SOL, then stop. Save a compact final report.
"@
    Write-Log "RUN $run begin"
    try {
        $prompt = Get-Content -LiteralPath (Join-Path $ScoutRoot 'AUTONOMOUS_SCOUT.md') -Raw
        $prompt = $prompt + "`r`n`r`n" + $continuation
        $prompt | & $Codex --ask-for-approval never --search exec --model gpt-5.6-luna --sandbox workspace-write -C $ScoutRoot -o $finalPath - 2>&1 | Tee-Object -FilePath $outputPath
        $exitCode = $LASTEXITCODE
        if ($exitCode -ne 0) { throw "Codex exited with status $exitCode" }
        $failures = 0
        Write-Log "RUN $run success final=$finalPath"
        & git -C $ScoutRoot status --short | Add-Content -LiteralPath (Join-Path $Autonomous 'supervisor.log')
        & git -C $ScoutRoot push origin $RemoteBranch 2>&1 | Add-Content -LiteralPath (Join-Path $Autonomous 'supervisor.log')
        if ($LASTEXITCODE -ne 0) { throw "git push exited with status $LASTEXITCODE" }
        Write-Log "RUN $run push success"
    } catch {
        $failures++
        Write-Log "RUN $run failure count=$failures error=$($_.Exception.Message)"
        if ($failures -ge $MaxConsecutiveFailures) {
            Write-Log 'Repeated failure limit reached; exiting.'
            break
        }
    }
    if ($run -lt $MaxRuns -and $SleepSeconds -gt 0) { Start-Sleep -Seconds $SleepSeconds }
}
Write-Log "END runs=$run failures=$failures"
