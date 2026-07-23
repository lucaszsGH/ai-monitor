# App download and privacy boundary

## Availability

The public repository currently provides the community Skill and synthetic demo. A stable Apple Silicon DMG should be attached to GitHub Releases only after the release checklist passes. Do not treat a source tag without a DMG asset as an App release.

## Supported baseline

- Apple Silicon Mac (M1 or newer)
- macOS 14 or later
- iPhone X through iPhone 17 Pro Max in landscape
- Claude Code, Codex, or both, installed and used locally

## What the App reads

AI Monitor reads privacy-filtered local status and usage summaries. It does not read or upload chat content. Provider availability differs: some figures are official account values, while others are locally derived and clearly labeled.

## Private LAN link

The dashboard uses a tokenized private link on the local network. A device must be on the same LAN and possess the full link to access it. Treat the link like a private viewing invitation: share it only when you intend another device or person on that network to view the summary.

The share actions in SET and the installation guide share only the public GitHub project page. They never share the LAN link, token, local address, real usage data, or session screenshot.

## Unsigned build

The current distribution is not Apple-notarized. Follow the visual guide included in the DMG to approve the App once in System Settings → Privacy & Security. Do not disable macOS security and do not run Terminal commands.
