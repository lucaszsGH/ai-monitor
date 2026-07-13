# Release Candidate Audit

Date: 2026-07-13
Candidate: `0.1.0-rc.2`
Scope: public package only

Product display name: **DeepWheel AI Monitor**. Home Screen short name: **AI Monitor**. The technical Skill identifier remains stable for compatibility.

## Requirement evidence

| Requirement | Evidence | State |
|---|---|---|
| Reusable Agent Skill | Skill entry, generator, validator, starter, bilingual docs, tests and CI are present | Proven locally |
| Strict 1:1 provider layout | Shared two-column grid plus negative/static test | Proven locally |
| Multiple sessions per provider | v2 provider/session contract, NOW and SESSIONS views | Proven locally |
| Account usage separated from session context | Contract invariant and negative validator test | Proven locally |
| DeepWheel visual system | Registered tokens, restrained blue, semantic colors, current bilingual hero and device renders | Proven locally |
| iPhone X through 17 Pro Max classes | Eight Home Screen landscape viewports, two browser endpoint classes, three views, Chinese/English, 100%/200% text scale, overflow, collision and bottom-gap assertions | 132 scenes proven in simulation; corrected v4 visual baseline accepted by the owner on an iPhone 17 Pro Max |
| Lucas-approved visual baseline | Exact accepted CSS baseline plus regression assertions for adaptive type, semantic quota colours, usage chart, shared session typography and NOW optical centering | Proven locally and owner-accepted on iPhone 17 Pro Max |
| New-user first success | Bilingual ten-minute guide, generated-folder README, trusted-LAN confirmation, Home Screen, stop and recovery steps | Proven in documented dry run |
| Public/privacy boundary | Neutral provider marks, synthetic fixture, path/credential-field rejection, no transcript reader | Proven locally |
| GitHub publishability | README, license, security, contribution, templates, workflow, examples and roadmap | Proven locally |
| Public visual consistency | Bilingual editable/rendered workflow pairs mirror the staged first-run guide and are bound to the current Skill/public inventory | Proven locally |
| Quality Gate | Current source gate reports CLEAN with no critical, warning or note findings after the public-surface binding | Proven locally |
| Private overlay isolation | Public validator contains no machine path; the separate standard private Skill candidate also passes the current source Quality Gate | Proven locally |

## External activation gates

These are not package defects, but remain outside local proof:

- Public neutral-starter rotation, Home Screen relaunch and long-running-display checks not explicitly covered by the v4 owner acceptance.
- Representative older-device real-hardware check; iPhone X coverage is currently simulated.
- GitHub repository creation and public visibility.
- Owner approval for commit, push, installation, Tag or Release.
- A Claude second-view review that returns usable review content.

## Release decision

The repository remains a **local GitHub release candidate**, not an installed or published release. Code, onboarding, bilingual public surfaces, the simulated device matrix and the iPhone 17 Pro Max visual acceptance pass locally. Publication remains blocked by separately authorized Git/GitHub actions; unchecked rotation, Home Screen relaunch and long-running-display evidence remain documented limitations rather than silently claimed proof.
