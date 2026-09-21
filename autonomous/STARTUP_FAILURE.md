# Startup failure

Date: 2026-09-14

The standalone clone and supervisor configuration were created on branch
`luna/k4-autonomous-scout`. Codex 0.154.0-alpha.6.2 starts with GPT-5.6 Luna at `xhigh`, live
search enabled, workspace-write requested, and the configured MCP servers disabled. The public
CIA search completed and no Unity/codex-imagen MCP startup error appeared.

Startup validation still could not pass after setting the child Codex working directory and
`--cd` to the standalone clone. The managed Windows sandbox rejected repository commands and the
temporary-file check with `apply deny-read ACLs`. The standalone clone has a real `.git` directory,
so this remains an execution-environment restriction rather than a worktree-pointer problem.

The supervisor was not detached and no overnight runs were started. Do not bypass this with
`danger-full-access`; rerun validation only after the Codex sandbox grants this exact directory
as a workspace-write root.

See `autonomous/validation-20260914-100548-luna-output.log` and
`autonomous/validation-20260914-100548-luna-final.md` for the complete worker record.
