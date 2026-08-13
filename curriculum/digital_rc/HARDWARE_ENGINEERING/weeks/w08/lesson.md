# Week 8: Devicetree overlay — I2C1 and LED0

Overlay enables &i2c1 status okay and led0 gpios. Deleting &soc is unsafe and fails. DT is the contract between board and drivers.

Lab checks overlay text and fields. No physical probe yet.

Show the week 8 arithmetic or parse fields the lab recomputes; GUI screenshots are not acceptance.

Overlay enables &i2c1 status okay and led0 gpios phandle. Deleting &soc is unsafe and fails. Devicetree is configuration-as-code: the lab parses overlay nodes, not a photo of a running LED. Keep the overlay usable in the EMBEDDED_PROTOTYPING subsystem packet.

Journal week 8 (Devicetree overlay — I2C1 and LED0): keep the artifact id, fixture counts, and computed fields; adjectives are not evidence.

Week 8 digital validators must pass before any PHYSICAL_PENDING soldering or instrument claim; show the arithmetic or parse fields the lab recomputes.

Week 8 digital validators must pass before any PHYSICAL_PENDING soldering or instrument claim; show the arithmetic or parse fields the lab recomputes.

## Worked example

i2c1_status=okay; led0_gpios set; overlay contains &i2c1 and led0.
