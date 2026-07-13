# Test Runs

## 2026-07-13 · viewport and first-run hardening

Status: local code, layout and bilingual public-surface checks pass; Lucas accepted the v4 public starter on an iPhone 17 Pro Max. Publication approval remains open.

Results:

- Public package validator: PASS.
- Unit tests: 9/9 PASS, including the DeepWheel app icon, bilingual switch, manifest name, Apple Home Screen name and the locked Lucas-approved visual baseline.
- Fresh generated starter: CLEAN; non-empty output remains protected from overwrite.
- First-run README is copied into the generated folder and contains localhost, trusted-LAN, Home Screen and stop/recovery guidance.
- Eight landscape viewport classes from 812×375 through 956×440 pass Chinese and English NOW / SESSIONS / USAGE in forced Home Screen mode.
- iPhone X and 17 Pro Max endpoint classes also pass in browser mode.
- Both 100% and simulated 200% root text scale pass without horizontal or vertical overflow: 66 bilingual scenes at each scale, 132 in total.
- The device harness now also rejects critical header, Provider-head, session-column and usage-main collisions, plus unsafe visible text overflow.
- Each checked `#app` bottom edge is within 0px of the measured viewport bottom; the harness fails above 1px.
- The owner confirmed on an iPhone 17 Pro Max that the shared `100dvh` / `100lvh` viewport correction removes the landscape bottom gap.
- After detecting that the public candidate had dropped 152 lines of accepted adaptive type, quota colour, usage-chart and optical-centering rules, the public starter was restored from the accepted private visual baseline. Lucas accepted the corrected v4 public starter on the real device.
- Bilingual workflow SVG/PNG pairs now match the staged first-run guide and were visually inspected after deterministic 1600×900 rendering.
- `PUBLIC-SURFACE-REVIEW.json` binds the exact packaged Skill and reviewed public-file inventory so later user-visible drift cannot silently pass.
- Current source Quality Gate: CLEAN with 0 critical, 0 warning and 0 note findings after the accepted v4 public assets and review fingerprint were refreshed.

The automated matrix simulates conservative safe areas and viewport sizes. iPhone X coverage remains simulated; exact hardware insets, Display Zoom, Dynamic Type and long-running display still require representative real-device checks.

## 2026-07-12 · local release-candidate baseline

Status: local automated baseline passed; real iPhone test pending.

Real-device finding: the first iPhone 17 Pro Max Safari check exposed two gaps—an absent `safe` query was incorrectly parsed as zero, and Safari chrome remained visible in a normal tab. The parser is fixed, the scene now uses a black base plus a conservative obstruction guard, and Apple standalone metadata and “Open as Web App” instructions were added. A second real-device check is pending.

Executed commands:

```bash
python3 scripts/validate-package.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 skills/lucas-deepwheel-ai-watchtower/scripts/create_watchtower.py --output <empty-temp-dir>
python3 skills/lucas-deepwheel-ai-watchtower/scripts/validate_watchtower.py <temp-dir>
```

Results:

- `validate-version.py`: PASS, version 0.1.0-rc.2.
- `validate-lucas-deepwheel-skill.py`: PASS.
- `validate-package.py`: PASS.
- Unit tests: 6/6 PASS.
- Generator succeeds in an empty directory: PASS.
- Generator blocks a non-empty directory: PASS.
- Clean starter returns exit code 0: PASS.
- Deprecated value and machine-path fixtures return concerns without echoing the private value: PASS.
- Generated starter validator: CLEAN.
- Quality Gate: CLEAN for the local release-candidate contents; external release activation gates remain pending.
- NOW, SESSIONS and USAGE render from one v2 contract; 956×440 and 812×375 logical samples were visually inspected.
- Provider-level usage inside a session is rejected by a negative test.
- The public fixture uses neutral Agent A / Agent B marks and contains no Claude or Codex trademark asset.
- Real iPhone landscape smoke test: pending.

## Device matrix simulation

Local Chrome layout smoke tests passed for NOW, SESSIONS and USAGE at both 100% and simulated 200% root text scale. The harness also injected conservative left/right and bottom safe-area values for:

```text
812×375  iPhone X class
844×390  iPhone 12/13/14 class
852×393  iPhone 14/15 Pro class
874×402  intermediate modern viewport guard
896×414  iPhone XR/XS Max/11 class
926×428  iPhone 12/13/14 Pro Max class
932×430  Plus/15 Pro Max class
956×440  iPhone 16/17 Pro Max physical 3× class
```

The simulated 200% run checks layout overflow only. Injected safe-area values check layout resilience but do not claim exact hardware insets. Neither simulation replaces iOS Dynamic Type, Safari Add to Home Screen, hardware safe-area, rotation, or long-running display tests on a real phone.

For a real-device spot check, append `?debug=1` to the page URL. The local-only overlay reports viewport, CSS safe-area insets, horizontal/vertical overflow and Home Screen display mode. It does not send or persist diagnostic data.

## Agent behavior evaluation

One paired run used the same user prompt with and without the Skill.

- With Skill: 5/5 assertions passed.
- Baseline without Skill: 4/5 assertions passed.
- The differentiating assertion was the explicit DeepWheel landscape contract: safe-area handling, landscape declaration, and registered brand blue.
- Both runs preserved demo-only data, avoided installation/overwrite, generated a previewable PWA, and explained phone access plus the read-only boundary.

Evaluation evidence is stored outside the public package under the local test workspace.

## Known render history

Earlier single-session and role-hierarchy samples were superseded. The current executable uses strict 1:1 Provider panels and three manual views: NOW for action priority, SESSIONS for up to four summaries per Provider, and USAGE for account-level consumption. Obsolete concept art was removed after owner approval. A headless Chrome compositor tile can affect some high-DPI SESSIONS screenshots; a clean 1× render and DOM overflow checks were used instead. This is a screenshot-tool artifact, not a measured layout overflow.
