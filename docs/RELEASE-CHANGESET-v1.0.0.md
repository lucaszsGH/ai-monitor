# AI Monitor v1.0.0 final release changeset

Status: local release materials prepared; no commit, push, tag, upload, or public release has been performed.

## Exact candidate

- Build: 21
- Platform: Apple Silicon, macOS 14+
- DMG: `AI-Monitor-1.0.0-build.21-macOS-arm64-unsigned.dmg`
- Size: `11,081,844` bytes
- SHA-256: `cd39ff4acd8477f55ba4612f36df33f5ff3e353f0e9220f11b7a8562dc35bff8`

## Public repository changes prepared

- Bilingual product value and installation guidance.
- Clear MIT-public-materials versus closed-App-binary license boundary.
- App download, privacy, security, trademark, contribution, Issue, and PR boundaries.
- Exact Build 21 release notes, audit evidence, checklist, and GitHub Release body.
- Community entry labels aligned to `GitHub · Star`, Feedback, and Share.

## Explicitly excluded

- Private runtime source and provider adapters.
- Credentials, tokens, private LAN links, local addresses, personal paths, logs, and real session data.
- Real usage screenshots or chat content.
- Apple Developer ID signing or notarization claims.

## External actions that still require separate approval

1. Commit the prepared public-repository changes.
2. Push the release branch.
3. Create and push tag `app-v1.0.0` so the App version does not conflict with the public Skill package version.
4. Create the GitHub Release and upload the exact DMG.
5. Download the public asset again and verify its SHA-256.

## Rollback boundary

Before publication, rollback is a local file revert. After publication, use a new corrective release or remove the Release asset only with explicit owner authorization; never silently replace a published binary under the same version.
