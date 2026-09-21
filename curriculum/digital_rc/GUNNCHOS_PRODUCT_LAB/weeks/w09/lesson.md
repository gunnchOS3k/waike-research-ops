# Week 9: Cross-repo dependency pin & telemetry honesty

**Ticket:** GPL-5909  
**Lab:** `lab_gpl_dep_pin`

## Objectives
- Refuse preview SHA in accepted-main pin
- Name pin_file
- NO_AI for pin authorship

## Body
Cross-repo dependency pins and telemetry share one honesty rule: accepted-main digests only. preview_sha_in_accepted must be false. Name the pin_file. NO_AI authorship for the pin.

Fabricated telemetry volumes ('millions of devices') fail the same honesty gate as fabricated community impact.
## Worked example
preview_sha_in_accepted=false, pin_file=CURRENT_ACCEPTED_MAIN.json

## Assessment mode
NO_AI

## Claim refusals
- No preview in accepted
- No fabricated telemetry volumes

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_gpl_dep_pin` and `GPL-5909`. Empty {} fails. A file whose body is only PASS raises.
