# Startup failure

Date: 2026-09-14

The standalone clone and supervisor configuration were created on branch
`luna/k4-autonomous-scout`. Codex 0.154.0-alpha.6.2 starts with GPT-5.6 Luna at `xhigh`, live
search enabled, workspace-write requested, and the configured MCP servers disabled. The public
CIA search completed and no Unity/codex-imagen MCP startup error appeared.

Startup validation could not pass because the managed Windows sandbox rejected every repository
read/write command aimed at `C:\Users\coler\Documents\Codex\k4-luna-scout-standalone` with
`apply deny-read ACLs`. The standalone clone has a real `.git` directory, so this is an execution
environment restriction rather than a worktree-pointer problem. The child could not verify git
status/log or create its temporary validation file.

The supervisor was not detached and no overnight runs were started. Do not bypass this with
`danger-full-access`; rerun validation only after the Codex sandbox grants this exact directory
as a workspace-write root.
