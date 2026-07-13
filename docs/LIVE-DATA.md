# Live data without credential scraping

DeepWheel AI Monitor deliberately separates three kinds of data:

1. **Session summaries** — sanitized titles, action, state, attention, and update time.
2. **Session context health** — a value for one session only, when a supported source exposes it.
3. **Provider usage** — account-level remaining usage, reset time, or credits from an official surface.

## Safe source order

1. Official documented status or usage surface.
2. User-authored structured summaries such as `CURRENT.md` or `HANDOFF.md`.
3. An audited adapter that emits only the v2 contract.
4. Manual entry.
5. `null` / unavailable.

Never scrape browser cookies, authentication files, private endpoints, raw transcripts, or complete terminal logs.

## Multiple sessions

An AI provider is a collection of sessions, not one giant session. The starter shows two highest-priority sessions on NOW, up to four per provider on SESSIONS, and account usage on USAGE. Context percentages stay attached to their own session and are never summed.

## Current provider surfaces

- Claude Code users can inspect account status with the supported authentication command and monitor allocation in Claude Code's official status surface. The public starter does not run those commands automatically.
- Codex users can inspect login status locally and view current usage in the Codex Settings usage surface. The public starter does not read authentication storage or undocumented endpoints.

Because product limits and interfaces change, adapter output must include a source and verification label. Unknown values remain `null`.

## Recommended private workflow

1. Ask the assistant to create a sanitized snapshot from recent task metadata and user-maintained continuity files.
2. Manually copy or enter official usage values if no documented machine-readable source exists.
3. Validate the snapshot.
4. Serve the PWA only on localhost or a trusted private network after explicit approval.

This keeps the public package reusable while allowing a private overlay to map machine-specific sources.
