# Review Record

## 2026-07-13 pre-release authorization

Lucas authorized the next public step after the AI Monitor rename and Quality Gate recheck. The authorization covers tag `v0.1.0-rc.3` and a GitHub Pre-release only; it does not authorize local Skill installation or a stable release. The exact pre-release candidate passed package, version, generic Skill, unit, device-matrix, public-surface and live GitHub/Actions reconciliation checks before activation.

## 2026-07-13 AI Monitor naming correction

Lucas confirmed that **AI Monitor** is the product name and **DeepWheel** is the brand and app-icon identity. The former repository, Skill ID, commands and public asset filenames were corrected before the first tagged release. The new public target is `lucaszsGH/ai-monitor`; Tag and GitHub Release remain separately gated.

The earlier Claude naming review is now historical because it reviewed the superseded compatibility decision. A fresh Claude second view is pending before a tagged Release. Codex therefore treats this change as owner-authorized and machine-verified, not Claude-approved.

## 2026-07-13 follow-up (superseded naming scope)

The confirmed product display name is **AI Monitor** and the Home Screen short name is **AI Monitor**. The official DeepWheel mark replaces the temporary `W` lettermark. Chinese and English share one app, follow the system language by default, and expose a compact stateless `EN／中` control.

| Review | Status | Evidence |
|---|---|---|
| X through 17 Pro Max layout | Passed in simulation | Eight Home Screen viewport classes, two browser endpoints, three views, 100%/200% text scale, no overflow, 0px measured bottom gap |
| iPhone 17 Pro Max viewport rule | Passed on owner device | The `100dvh` / `100lvh` split removed the observed landscape bottom gap |
| New-user first success | Passed for documented dry run | Bilingual ten-minute guide, generated-folder README, trusted-LAN confirmation, Home Screen steps, stop and recovery guidance |
| Public package and tests | Passed locally | Package validator, 9/9 unit tests, fresh generation and generated-starter validation |
| Public visual consistency | Passed locally | English and Chinese editable SVG plus rendered PNG workflow pairs now mirror the staged first-run path; the public-surface review manifest binds the exact Skill and reviewed inventory |
| Current source Quality Gate | CLEAN | 0 critical, 0 warning and 0 note findings after public-surface binding |
| Claude second view | Passed with concerns accepted | No P0; the earlier real-device P1 is now resolved by the v4 owner pass, and the public review inventory was expanded per P2 |
| Naming second view | Passed after repair | Claude found the Apple Home Screen meta name still said `DeepWheel`; it now matches `AI Monitor` and is protected by validator and unit-test assertions |
| Owner visual baseline | Passed on iPhone 17 Pro Max | Lucas accepted v4 after the public starter was restored to the approved private typography, semantic quota colours, usage structure and NOW optical centering |
| Public repository | Live | Public GitHub repository exists; Tag and GitHub Release remain pending |

The current product judgment is to keep the candidate demo-first. Live adapters, background services and private networking remain separate opt-in layers rather than part of first run. The revised public workflow makes the safe order explicit: synthetic demo, local validation, desktop preview, separately confirmed trusted-LAN sharing, iPhone check, then optional read-only data work. The accepted private visual baseline is now a regression-locked public contract rather than a direction for further redesign.

## Release candidate 0.1.0-rc.2

| Review | Status | Evidence |
|---|---|---|
| Package structure | Passed locally | Version, package and Skill validators pass; 6/6 unit tests pass |
| Security and privacy | Passed for public static baseline | No private overlay, absolute path or credential-shaped assignment found; live adapters remain disabled |
| DeepWheel visual contract | Passed for refined executable samples | Pure-black device base, strict 1:1 Provider layout, dark DeepWheel surfaces, restrained blue, semantic green/orange/red, neutral public marks, and NOW/SESSIONS/USAGE hierarchy |
| Accessibility | Passed static and simulated layout baseline; device recheck pending | CSS safe-area plus 44–62pt obstruction guard, 44px navigation targets, reduced motion, and all three views across eight viewports at simulated 100%/200% root text scale pass without layout overflow |
| iPhone landscape | First real-device check found Dynamic Island overlap and Safari chrome; fixes applied, recheck pending | Black base and obstruction guard now protect content; standalone/Home Screen metadata and instructions added |
| Third-party license | Passed for bundled code | No third-party source or asset was copied into the package; external projects are references only |
| Public/private separation | Passed locally | Public package validator rejects machine paths; private overlay is stored outside the repository candidate |
| Final owner approval | Pending | Required before push or public release |

Machine checks do not replace the iPhone, accessibility, privacy, or owner sign-off.

## Claude second-view attempt

- Scope was limited to the public candidate.
- Claude Code was invoked twice in read-only/non-editing modes.
- Both runs returned no review content, so no Claude approval is claimed.
- See `docs/CLAUDE-CO-REVIEW.md`.

## Paired behavior evaluation

- With Skill: 5/5 deterministic assertions passed.
- Without Skill: 4/5 passed.
- Skill-specific gain: DeepWheel landscape contract was explicit and machine-detectable.
- Timing/token comparison was not available from the evaluation runner and is not claimed.

## Seven-role review summary

### 1. Developer

- Passed: small standard-library scripts, deterministic output, no overwrite, tests and CI.
- Largest risk: live provider adapters remain mapping contracts rather than bundled automatic collectors.
- Recommendation: keep adapters optional, one-way, and behind the v2 status contract.
- Severity: advisory.

### 2. New user

- Passed: demo-data first success needs no provider login or package install.
- Largest risk: the first real-data refresh is assistant-assisted or manual until a private service is approved.
- Recommendation: add a guided trusted-LAN recipe only after device validation.
- Severity: warning before 0.2.

### 3. Experienced GitHub user

- Passed: bilingual README, installation, security, contribution, examples, CI and roadmap exist.
- Largest risk: no repository history, release, Tag or public URL yet.
- Recommendation: publish only after owner approval and clean checklist.
- Severity: release blocker by policy, not a package defect.

### 4. GitHub auditor

- Passed: public/private separation, synthetic data, no third-party code copied, no automatic network exposure.
- Largest risk: future adapters could introduce credential or transcript access.
- Recommendation: require per-adapter permission and supply-chain review.
- Severity: warning for future adapters.

### 5. High-star Skill evaluator

- Passed: clear problem, three useful views, multiple-session model, visual demo, reusable contract and recovery path.
- Largest risk: the current release demonstrates the screen and mapping contract but not automatic live collection.
- Recommendation: ship 0.1 honestly as demo-first, then add one audited, opt-in adapter.
- Severity: advisory.

### 6. Token-sensitive user

- Passed: static files, synthetic fixture, no transcript scan, no default AI call.
- Largest risk: future full-history parsing would violate the low-cost promise.
- Recommendation: keep summaries user-authored or event-based.
- Severity: advisory.

### 7. iOS experience reviewer

- Passed: landscape-first hierarchy, short labels, manual view switching, safe-area variables, 44px navigation targets and clear unavailable-state path.
- Largest risk: v4 visual acceptance exists on iPhone 17 Pro Max, but rotation, Home Screen relaunch and long-running display were not explicitly included in that acceptance.
- Recommendation: keep those three unchecked limitations visible until representative evidence is recorded.
- Severity: release warning.
