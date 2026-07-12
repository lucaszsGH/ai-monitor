# Test Runs

## 2026-07-12 · local release-candidate baseline

Status: local automated baseline passed; real iPhone test pending.

Executed commands:

```bash
python3 scripts/validate-package.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
python3 skills/lucas-deepwheel-ai-watchtower/scripts/create_watchtower.py --output <empty-temp-dir>
python3 skills/lucas-deepwheel-ai-watchtower/scripts/validate_watchtower.py <temp-dir>
```

Results:

- `validate-version.py`: PASS, version 0.1.0-rc.1.
- `validate-lucas-deepwheel-skill.py`: PASS.
- `validate-package.py`: PASS.
- Unit tests: 4/4 PASS.
- Generator succeeds in an empty directory: PASS.
- Generator blocks a non-empty directory: PASS.
- Clean starter returns exit code 0: PASS.
- Deprecated value and machine-path fixtures return concerns without echoing the private value: PASS.
- Generated starter validator: CLEAN.
- Quality Gate: CLEAN for the local release-candidate contents; external release activation gates remain pending.
- Executable renders at 956×440 and 812×375 logical points: visually inspected and accepted as the current equal-split samples.
- Real iPhone landscape smoke test: pending.

## Device matrix simulation

Local Chrome layout smoke tests passed at both 100% and simulated 200% root text scale. The harness also injected conservative left/right and bottom safe-area values for:

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

## Agent behavior evaluation

One paired run used the same user prompt with and without the Skill.

- With Skill: 5/5 assertions passed.
- Baseline without Skill: 4/5 assertions passed.
- The differentiating assertion was the explicit DeepWheel landscape contract: safe-area handling, landscape declaration, and registered brand blue.
- Both runs preserved demo-only data, avoided installation/overwrite, generated a previewable PWA, and explained phone access plus the read-only boundary.

Evaluation evidence is stored outside the public package under the local test workspace.

## Known render history

The first local render did not keep the action bar in the 430px viewport. The second fixed-height attempt showed a headless-browser overflow compositing artifact. Iteration 3 fixed layout but remained visually too uniform. Two image2 passes then informed the refined direction; the executable implementation was rebuilt as a strict 1:1 peer-agent layout with green working state, orange waiting state, circular Context gauges, linear Quota bars and one blue action focus. All superseded samples were removed after owner approval.
