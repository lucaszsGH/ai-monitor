# Private Overlay

The public package must remain generic and synthetic. Personal configuration belongs in a separate local directory or private repository.

## Private-only examples

- machine-specific paths;
- real project and workspace names;
- account labels;
- actual work objectives, blockers, and next actions;
- local status-adapter commands;
- private-network hostnames;
- notification routing.

## Still forbidden

Even the private overlay must not store reusable credentials, browser cookies, session keys, passwords, private keys, verification codes, or complete sensitive logs.

## Merge direction

Public core may be copied into a private runtime build. Private data must never flow back into the public repository, screenshots, test fixtures, Issues, pull requests, or Releases.

