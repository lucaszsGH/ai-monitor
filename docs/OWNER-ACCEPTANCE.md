# Owner Acceptance

This checklist separates real-device acceptance from installation and publication.

## iPhone landscape acceptance

- [x] Open the local preview in Safari on the same trusted network.
- [ ] Add it to the Home Screen with **Open as Web App** enabled.
- [ ] Launch from the Home Screen icon and confirm Safari chrome is absent.
- [ ] Rotate both landscape directions and confirm the notch or Dynamic Island merges into the black edge.
- [ ] Confirm no text, icon, card or navigation target enters the obstruction guard.
- [x] Switch NOW, SESSIONS and USAGE; confirm both Provider panels remain strict 1:1 peers.
- [x] Confirm Chinese labels are readable at the user's normal text size.
- [ ] Leave the screen active for the intended test period and confirm no destructive burn-in-like static emphasis or distracting animation.
- [x] On the public neutral starter, append `?debug=1` and confirm PASS plus no bottom gap.

Owner evidence recorded on 2026-07-13: Lucas accepted the v4 public neutral starter on an iPhone 17 Pro Max after checking the corrected private-baseline typography, semantic quota colours, three-view navigation and compact language switch. Unchecked rotation, Home Screen relaunch and long-running-display items remain intentionally unclaimed.

## Candidate acceptance

- [x] Public package uses synthetic data and neutral provider marks.
- [x] Private overlay is outside the public repository.
- [x] Public and private validators pass locally.
- [x] Current source Quality Gate reports CLEAN after the bilingual public-surface review.
- [x] Owner accepts the final real-device appearance.

## Action boundaries

Each action requires a separate explicit approval:

- [x] Amend or create the local release-candidate commit.
- [ ] Install the Skill locally.
- [ ] Create or configure the GitHub repository.
- [ ] Push `main`.
- [ ] Make the repository public.
- [ ] Create a Tag or Release.

Unchecked action boxes are intentional and do not prevent local candidate testing.
