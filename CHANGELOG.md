# Changelog

## [Unreleased]

### Added

- Bilingual ten-minute first-run guides and a self-contained generated-folder README.
- Trusted-LAN confirmation, Home Screen setup, stop/recovery, and common failure guidance.
- Device-matrix assertions for browser/Home Screen viewport modes and bottom-gap detection.

### Changed

- Browser mode now uses `100dvh`; iOS Home Screen mode uses `100lvh` while preserving safe-area padding.
- New-user flow now separates demo generation, desktop validation, desktop preview, trusted-LAN confirmation, phone checks, and optional live-data work.
- Bilingual workflow visuals now present the same safe first-run order and distinguish trusted-LAN sharing from optional live-data access.
- The public product display name is now **DeepWheel AI Monitor**, with the short Home Screen name **AI Monitor** and the official DeepWheel app icon.
- The interface now follows the system language by default and offers a compact stateless `EN／中` switch.
- The public starter now inherits the Lucas-approved private visual baseline instead of maintaining a separate public redesign: adaptive landscape type, semantic remaining-quota colours, the accepted usage chart, shared session alignment and NOW optical centering.

### Fixed

- Restored accepted visual rules that had been dropped from the public candidate and added regression assertions for visual tokens, thresholds, critical component collisions and unsafe visible text overflow.

### Planned

- Optional, audited read-only adapters.
- Private-network deployment recipe.

## [0.1.0-rc.2] - 2026-07-12

### Added

- Multi-session v2 contract with NOW, SESSIONS and USAGE views.
- Provider-level usage and session-level context separation.
- Conservative 44–62pt landscape obstruction guards and local device diagnostics.
- Apple Web App metadata and Home Screen full-screen guidance.
- Private-overlay preview generator and redaction contract.

### Changed

- Default iPhone scene now uses a pure-black base and dark DeepWheel surfaces so the notch or Dynamic Island visually merges into the edge.
- Public provider marks are neutral; provider trademarks remain in the private overlay only.

### Fixed

- Missing `safe` query values no longer parse as zero and disable the device obstruction guard.

## [0.1.0-rc.1] - 2026-07-12

### Added

- Public Agent Skill entrypoint.
- Privacy-safe status data contract.
- DeepWheel landscape mobile UI contract.
- Demo-data PWA starter.
- Non-overwriting generator and static validator.
- Bilingual documentation, security policy, tests, CI, and private-overlay boundary.
