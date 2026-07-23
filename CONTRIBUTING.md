# Contributing

Thank you for helping improve AI Monitor.

This repository is the public collaboration layer. Pull requests can improve documentation, device profiles, the public Skill, synthetic demos, validators, status contracts, and adapter examples. The private macOS runtime is maintained separately and is not required for useful community contributions.

## Before opening a pull request

1. Keep the default product read-only and demo-data first.
2. Do not add credentials, real transcripts, private paths, customer data, or complete logs.
3. Keep provider adapters behind the public status contract.
4. Add positive and negative tests for generator or validator changes.
5. Run:

```bash
python3 scripts/validate-package.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## Design contributions

Preserve the DeepWheel landscape contract: one blue focus per screen, restrained color, safe areas, 44px targets, readable text scaling, and no deprecated values.

The maintained device baseline covers iPhone X through iPhone 17 Pro Max in landscape. For iPadOS, Android, unusual scaling, or other screens, open a feature request with the physical device, OS version, browser / Home Screen mode, and synthetic-data screenshot. The maintainer may provide a free compatibility adjustment when reproducible evidence is available.

## Public / private boundary

- Do not request or submit the private macOS runtime.
- Do not attach the downloadable App binary to a pull request.
- Do not copy provider credentials, undocumented authenticated endpoints, or machine-specific adapters into the public repository.
- Public examples must use synthetic provider names, paths, sessions, and usage values.

## License compatibility

Do not copy third-party code or assets without a compatible, verified license and attribution. AGPL-derived work must not be mixed into this MIT package without an explicit licensing decision.
