# Adapter contract

An adapter is a one-way sanitizer. It converts an approved source into `schema_version: 2.0`; it is not a remote-control bridge.

## Required behavior

- Emit at most two providers in the default phone view.
- Use opaque session IDs; never expose local database IDs or file paths.
- Limit titles and actions to short summaries.
- Mark every usage and context value with a source.
- Preserve `null` for unknown values.
- Write to a temporary file, validate, then atomically replace the prior snapshot.
- On failure, retain the last valid snapshot and show the source as unavailable.

## Forbidden input and output

- credentials, API keys, tokens, cookies, passwords, private keys;
- authentication files or headers;
- transcript or prompt bodies;
- complete logs or stack traces;
- absolute paths, customer names, private account identifiers;
- undocumented provider endpoints.

## Public versus private

The public repository contains only this interface, neutral synthetic fixtures, validators, and setup guidance. Machine-specific mappings, real project labels, network addresses, schedules, and official-account usage values belong in a private overlay outside the repository.
