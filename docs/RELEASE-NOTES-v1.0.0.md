# AI Monitor 1.0.0

Target: Apple Silicon Macs on macOS 14 or later, plus iPhone X through iPhone 17 Pro Max in landscape.

## What it gives you

- A persistent Claude + Codex side screen on an iPhone beside the Mac.
- Waiting/running/review status without opening every session.
- Subscription limits, usage diagnosis, and model share views.
- Claude-only, Codex-only, and dual-tool modes.
- Local processing without reading chat content.

## Build 21

- Keeps the Lucas-approved V28 dashboard UI unchanged.
- Uses a locked Python 3.14.6 / OpenSSL 3.5.7 arm64 build environment.
- Requires a tokenized private LAN link and rejects untrusted loopback Host headers.
- Bundles the visual install guide, binary license, third-party notices, and runtime licenses.
- Labels the public project action as **GitHub · Star** in both the install guide and first-run setup.

## Installation boundary

This stable build is not Apple-notarized. Read the visual guide bundled with the DMG and approve AI Monitor once in System Settings → Privacy & Security. Do not disable macOS security and do not run Terminal commands.

## Release artifact

- File: `AI-Monitor-1.0.0-build.21-macOS-arm64-unsigned.dmg`
- Size: `11,081,844` bytes
- SHA-256: `cd39ff4acd8477f55ba4612f36df33f5ff3e353f0e9220f11b7a8562dc35bff8`

Verify the checksum before opening the DMG. This candidate has not been uploaded to GitHub Releases yet.

## Privacy boundary

The dashboard uses a tokenized private LAN link. Only devices on the same network with the full link can access it. SET and guide share actions publish only the public GitHub project page; they never share the private link, token, local address, usage data, or session screenshots.

## Source boundary

Public repository materials remain under the MIT License unless a file says otherwise. The downloadable App binary contains a private local runtime and uses the separate license bundled with the App.

## Known limitations

- Provider data availability differs. Unavailable or locally derived values are labeled instead of being presented as official.
- The unsigned build requires a one-time macOS approval.
- Intel Macs and macOS 13 or earlier are not supported.
