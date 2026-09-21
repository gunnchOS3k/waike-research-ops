# Week 8: Devicetree overlay — buses and LEDs without deleting SoC

**Ticket:** EP-4808  
**Lab:** `lab_ep_dt_overlay`

## Objectives
- Enable &i2c1 and led0 in overlay
- Refuse delete_soc
- Treat DT as the hardware/software interface contract

## Body
Devicetree overlays name hardware for firmware. Enable &i2c1 and led0. delete_soc=true is unsafe and fails. This overlay is the HW/SW interface contract that higher layers (including Device OS guests) will assume.

No-hardware fallback: overlay fixture check. Claiming board bring-up complete from overlay text alone fails honesty.
## Worked example
overlay_has_i2c1=true, overlay_has_led0=true, delete_soc=false

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No deleting &soc
- No claiming board bring-up complete from overlay alone

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_ep_dt_overlay` and `EP-4808`. Empty {} fails. A file whose body is only PASS raises.
