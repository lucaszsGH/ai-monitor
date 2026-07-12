# Security Policy

## Sensitive data

Do not store, commit, echo, or publish credentials, cookies, session material, passwords, private keys, verification codes, one-time login data, complete sensitive logs, full conversations, or private customer material.

Findings must name only the risk category and relative file. Never print a matched value.

## Network boundary

The starter is a read-only status screen. Do not expose its local server directly to the public internet. Use authenticated HTTPS or a private network only after explicit user confirmation.

Remote approval and arbitrary command execution are outside the default product boundary and require a separate threat model.

## Private overlay

Machine-specific paths, account labels, internal project names, real work context, and local adapters belong in a local private overlay outside this public repository.

## Restricted actions

This Skill must not automatically install software, upload files, send messages, modify network visibility, publish a repository, push, create a Tag or Release, or overwrite an existing output directory.

## Reporting

Report vulnerabilities privately to the repository owner. Do not include reusable login material or private source data in an Issue.

