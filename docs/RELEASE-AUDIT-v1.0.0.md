# AI Monitor 1.0.0 release-candidate audit

Audit date: 2026-07-23
Candidate: macOS Build 21, Apple Silicon, macOS 14+

## Verified

- Private runtime and public collaboration source remain separate.
- The Lucas-approved V28 UI hashes are unchanged by Build 21.
- UI Guard full matrix remains bound to the current V28 files: 176 scenarios, 4,009 checks, 0 failures.
- Private unit suite: 81 tests, 0 failures.
- Public package validator and unit suite: 9 tests, 0 failures.
- Public iPhone device matrix passed at 100% and 200% font scale.
- Six hashed PyPI build dependencies match the lock.
- The built App contains the binary license, third-party notices, and official Python runtime license inventory.
- All 53 bundled Mach-O files are arm64 and declare macOS 14 or earlier as their minimum.
- DMG checksum, ad-hoc signature, Finder layout, visual guide, and packaged privacy boundary passed.
- The exact Build 21 artifact includes **GitHub · Star** in both the install guide and first-run setup.
- Lucas accepted the Build 21 local installation result.

## Exact artifact

- `AI-Monitor-1.0.0-build.21-macOS-arm64-unsigned.dmg`
- Size: `11,081,844` bytes
- SHA-256: `cd39ff4acd8477f55ba4612f36df33f5ff3e353f0e9220f11b7a8562dc35bff8`

## Remaining owner gate

Lucas must separately approve the public Git commit/push, `app-v1.0.0` tag, GitHub Release creation, and DMG upload. The `app-` prefix keeps the App version distinct from the public Skill package, which remains `0.1.0-rc.3`. Preparing these materials does not perform any of those actions.

The App is ad-hoc signed, not Apple Developer ID signed or notarized. Provider mark review follows public guidance and attribution boundaries; it is not a legal opinion.
