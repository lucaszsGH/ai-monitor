# AI Monitor binary release checklist

The public repository and the private runtime have separate responsibilities. A release is ready only when every required item below has current evidence.

- [x] Version, build number, release date, and SET label agree.
- [x] Apple Silicon only; every bundled Mach-O is arm64 and supports macOS 14.
- [x] Locked build dependencies and hashes reproduce the bundle.
- [x] App binary license, third-party notices, and official runtime license texts are included.
- [x] Provider trademark use follows current official guidance and retains attribution / non-affiliation language.
- [x] No credentials, private links, tokens, real session screenshots, chat content, private paths, or sensitive logs are present.
- [x] Claude-only, Codex-only, and dual-tool refresh behavior is covered by automated tests.
- [x] 896×414 Chinese and 812×375 Chinese/English browser checks pass.
- [x] iPhone X through iPhone 17 Pro Max device matrix passes at 100% and 200% font scale.
- [x] First-run setup, private-link copy, Add to Home Screen guidance, overwrite upgrade, and stop/restart paths have automated coverage.
- [x] DMG mounts, Finder layout is intact, the visual guide opens, and the App passes ad-hoc signature verification.
- [x] The install guide and first-run page label the community action as `GitHub · Star`.
- [x] SHA-256 and release notes were generated from the exact Build 21 DMG.
- [x] Lucas accepted the exact Build 21 local installation result.
- [ ] Lucas has separately approved the Git commit/push.
- [ ] Lucas has separately approved the `app-v1.0.0` tag, GitHub Release, and DMG upload.
