# Week 7: UPS runtime — watt-hours, inverter loss, and a graceful shutdown

ISH-4707: the community centre's storage box and router should ride out short power cuts and shut down cleanly during long ones. A battery's energy is in watt-hours, and the uninterruptible power supply converts it back to mains power through an inverter that loses some energy as heat. This unit holds two 12 V, 36 Ah batteries, about 864 Wh, and its inverter is about 85 percent efficient. The load measured at the wall is 300 W, so the runtime is 864 × 0.85 ÷ 300 hours, about 2.45 hours or 146.9 minutes. Batteries age, cold rooms reduce capacity, and the last minutes of a discharge are not reliable, so the bench starts a graceful shutdown no later than 80 percent of the computed runtime; here the plan picks 110 minutes. Configure the storage box to listen for the UPS's low-battery signal over USB or the network, and test it by pulling the plug while someone watches. Never plug a laser printer or a space heater into the battery outlets; their surges can overload the inverter.

## Worked example

864 Wh × 0.85 / 300 W × 60 = 146.9 min; start shutdown by 80% → no later than about 117 min (bench picks 110)
