# Week 5: Fault isolation — symptom first, subsystem second, parts last

ISH-4505 is five machines on the bench at once and a temptation to start swapping motherboards. Good technicians follow the power-on sequence, because each stage that succeeds rules out everything before it. No lights and no fans means the power path: the outlet, the cable, the supply's rear switch, then the supply itself. Fans spinning with beeps and no picture means the board is alive but the self-test failed, most often memory or a processor that is not seated; reseat the sticks one at a time before anything else. A self-test that passes and then complains there is no boot device points at the boot order in the firmware or a disk that is not detected. A machine that boots and then shows a stop error usually blames the last driver or update installed. Random shutdowns only under heavy load suggest heat or an undersized supply, so check temperatures and last week's power budget. Write down the symptom in the customer's words, the stage it fails at, and the cheapest test that would confirm your guess. Replacing parts before isolating the fault costs money and hides the real cause.

## Worked example

T1 fans/no display/beeps → memory_or_cpu_seating; T2 dead → power_path; T3 shuts down under load → thermal_or_psu_capacity; T4 no boot device → boot_order_or_disk; T5 stop error after boot → driver_or_os
