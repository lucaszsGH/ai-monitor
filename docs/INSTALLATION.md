# Installation

## Requirements

- Python 3.10 or later for the bundled generator and validator.
- A modern browser for preview.
- No Node.js, package install, provider login, or network service is required for the demo starter.

## Manual Skill installation

Copy only the Skill package into a supported local Skills directory after reviewing it:

```text
skills/lucas-deepwheel-ai-watchtower/
```

The exact destination depends on the host application. Do not overwrite an existing installed copy without a backup and explicit confirmation.

## First success

Generate a demo into a new directory and validate it. This confirms the Skill works without reading any real Claude/Codex data.

## Optional tools

Live provider status, HTTPS, private-network access, push notifications, or background launch require separate tools and permissions. Before enabling one, explain:

```text
What will be installed or enabled
Why it is needed
What data it can access
How to proceed without it
How success and rollback will be verified
```

Never install optional tools automatically.

## Uninstall

Remove the copied Skill directory only after confirming it is the intended copy. Generated Watchtower folders are independent and are not deleted automatically.

