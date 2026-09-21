# Week 2: Architecture & compatibility matrix (device-os × gunnchAI)

**Ticket:** GPL-5202  
**Lab:** `lab_gpl_compat_matrix`

## Objectives
- Pin accepted-main SHAs only
- Record contract_ok from versioned check
- Refuse preview SHAs in accepted pins

## Body
Architecture here is the compatibility contract between gunnchos-device-os and gunnchAI pins. Use accepted-main pair digests only. Unmerged PRs (including device-os #103 class) are not Product-Use evidence.

Industrial design interaction: note form-factor constraints as requirements inputs — do not invent physical EVT photos.

## Worked example
device_os_sha=d5c2d17, gunnchai_sha=d357846, contract_ok=true

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No unmerged PR as accepted pin
- No fabricated hardware EVT photos

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_gpl_compat_matrix` and `GPL-5202`. Empty {} fails. A file whose body is only PASS raises.
