# Week 7: Release engineering — semver & breaking flags

**Ticket:** GPL-5707  
**Lab:** `lab_gpl_release_notes`

## Objectives
- Ship semver with explicit breaking flag
- Require changelog_entries ≥ 1
- Tie release notes to docs consumers

## Body
Release eng is product work: semver, breaking_change boolean, changelog. Docs must match the flag. Industrial design interaction appears as 'breaking for enclosure fit' only when true and evidenced.

## Worked example
semver=1.4.0, breaking=false, changelog_entries=3

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No silent breaking changes
- No cert grant via release notes

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_gpl_release_notes` and `GPL-5707`. Empty {} fails. A file whose body is only PASS raises.
