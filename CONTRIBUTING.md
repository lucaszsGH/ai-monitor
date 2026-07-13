# Contributing

Thank you for helping improve AI Monitor.

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

## License compatibility

Do not copy third-party code or assets without a compatible, verified license and attribution. AGPL-derived work must not be mixed into this MIT package without an explicit licensing decision.

