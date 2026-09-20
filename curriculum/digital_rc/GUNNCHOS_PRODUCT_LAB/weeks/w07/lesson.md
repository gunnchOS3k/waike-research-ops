# Week 7: Release engineering — semver & breaking flags

**Ticket:** GPL-5707  
**Lab:** `lab_gpl_release_notes`

## Objectives
- Ship semver with explicit breaking flag
- Require changelog_entries ≥ 1
- Tie release notes to docs consumers

## Body
Release engineering is customer-facing truth: semver, explicit breaking flag, changelog entries. Docs consumers (desk leads, volunteers) must see the same breaking_change boolean the CI gate saw.

If enclosure fit would break, say so with evidence; do not invent industrial-design EVT photos.
## Worked example
semver=1.4.0, breaking=false, changelog_entries=3

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No silent breaking changes
- No cert grant via release notes

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_gpl_release_notes` and `GPL-5707`. Empty {} fails. A file whose body is only PASS raises.
