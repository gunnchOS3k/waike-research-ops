# Week 6: Hardware triage — power, then storage, then memory, then OS

The Civic Tech Desk keeps a parts tub: one spare 16 GB SODIMM, one SATA SSD, one 90 W brick, one display cable. Swapping before naming the subsystem is how you waste the only DIMM. Order of operations: confirm power (brick voltage and LED), then listen and SMART for storage, then count RAM in the firmware screen, then accuse the OS.

POST beep patterns are not folklore you invent. No display plus fans plus a single short beep on this classroom board means 'alive but video path.' Reseat RAM and check the display cable before you reinstall Windows. Reinstall is an OS move and this is still a hardware week.

Mobile devices appear as patrons' phones tethering the kiosk 'because Wi-Fi is slow.' You will check the kiosk Ethernet link lights before you blame the phone. A+ V15 Core 1 cares about mobile accessories; this desk cares that a phone hotspot is not a substitute for a dropped patch cable under the table.

Thermal ticket 4418 returns: dust in the intake, fan RPM in the BIOS, and a surface thermometer reading 78 C at the exhaust. Clean, then re-measure. Buying a new chassis is not a lab step.

## Learn the distinction

Power delivery, storage, working memory and software can each prevent a device from completing a task. A diagnostic sequence is a hypothesis-testing strategy, not a rule that the same component always fails first. RAM generally holds active working data; persistent storage holds saved data across ordinary shutdowns. Available storage and available memory are different measurements.

## Guided practice: calculate before deleting

For the classroom volume, size is 256 GiB, used data 180 GiB and separately reserved space 12 GiB. Subtract used and reserved space: 64 GiB usable free. Divide 64 by 256 to get 0.25, or 25%. Now change used data to 210 GiB: usable free is 34 GiB, about 13.28125%, below the fixture's 15% policy. Use the browser calculator to test both predictions. Expected result: the two cases fall on opposite sides of the policy threshold.

On a device you own, identify the operating system's storage view and note the displayed units. Do not combine GB and GiB without conversion. Do not subtract a reserve twice if the operating system's available-space number already accounts for it. Read-only observation is sufficient; deleting files is not required.

## Independent evidence

Produce a triage table with observation, hypothesis, safe test and stop condition for a no-power report and a slow-application report. A swollen battery, unusual heat or damaged power cable requires stopping and seeking qualified assistance. Do not open mains-powered equipment.

## Check your reasoning

A single slow launch does not establish a failing disk. Repeated measurements under comparable conditions and relevant system logs are stronger evidence. Record uncertainty instead of naming an unsupported cause.

## Worked example

No video, fans spin, one short beep, Ethernet lights off because you pulled the PC out. Restore the display cable and the patch cable before you unbox the spare SODIMM.
