# Week 7: Zephyr west + QEMU before hardware

west build -b qemu_cortex_m0 for the ForgeSense app. physical_status must be PHYSICAL_PENDING. qemu_ok true after digital run log fixture. Zephyr docs OPEN_LICENSE / reference — we do not vendor the entire tree.

EMBEDDED_PROTOTYPING integration: same app will bind I2C in DT next week.

Show the week 7 arithmetic or parse fields the lab recomputes; GUI screenshots are not acceptance.

west build -b qemu_cortex_m0 for the ForgeSense app. physical_status must remain PHYSICAL_PENDING until digital build and QEMU boot logs pass. Claiming board flashed without hardware evidence fails. Zephyr docs are PUBLIC_REFERENCE_ONLY; your west/CMake fragments are original WAIKE wording for ForgeSense.

Journal week 7 (Zephyr west + QEMU before hardware): keep the artifact id, fixture counts, and computed fields; adjectives are not evidence.

Week 7 digital validators must pass before any PHYSICAL_PENDING soldering or instrument claim; show the arithmetic or parse fields the lab recomputes.

## Worked example

board=qemu_cortex_m0 west_cmd includes west build -b qemu_cortex_m0; PHYSICAL_PENDING; qemu_ok true.
