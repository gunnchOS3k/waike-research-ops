# Week 5: ADC scaling — counts to millivolts

**Ticket:** EP-4505  
**Lab:** `lab_ep_adc_scale`

## Objectives
- Convert 12-bit counts to mV with stated vref
- Show the arithmetic, not a GUI needle
- Tie actuators/sensors to scaled units in the journal

## Body
raw=2048 on a 12-bit ADC with vref_mv=3300 yields about 1650 mV using the fixture convention mv ≈ raw * vref / (2^bits - 1) (lab accepts ±50 mV). Show the arithmetic in the JSON; a GUI needle screenshot is not acceptance.

Sensors feed actuators: driving a motor from unscaled counts is a latent hazard. No-hardware fallback uses fixture raw values. Do not claim metrology-lab calibration.
## Worked example
raw=2048, vref_mv=3300, resolution_bits=12, mv=1650

## Assessment mode
AI_DISCLOSED

## Claim refusals
- No claiming calibrated metrology lab accuracy
- No fabricated sensor field readings

## Journal prompt
Restate the worked numbers, name one claim you refuse from the list above, and keep prose specific to `lab_ep_adc_scale` and `EP-4505`. Empty {} fails. A file whose body is only PASS raises.
