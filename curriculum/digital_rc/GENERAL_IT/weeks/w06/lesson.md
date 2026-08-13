# Week 6: Hardware triage — power, then storage, then memory, then OS

The Civic Tech Desk keeps a parts tub: one spare 16 GB SODIMM, one SATA SSD, one 90 W brick, one display cable. Swapping before naming the subsystem is how you waste the only DIMM. Order of operations: confirm power (brick voltage and LED), then listen and SMART for storage, then count RAM in the firmware screen, then accuse the OS.

POST beep patterns are not folklore you invent. No display plus fans plus a single short beep on this classroom board means 'alive but video path.' Reseat RAM and check the display cable before you reinstall Windows. Reinstall is an OS move and this is still a hardware week.

Mobile devices appear as patrons' phones tethering the kiosk 'because Wi-Fi is slow.' You will check the kiosk Ethernet link lights before you blame the phone. A+ V15 Core 1 cares about mobile accessories; this desk cares that a phone hotspot is not a substitute for a dropped patch cable under the table.

Thermal ticket 4418 returns: dust in the intake, fan RPM in the BIOS, and a surface thermometer reading 78 C at the exhaust. Clean, then re-measure. Buying a new chassis is not a lab step.

## Worked example

No video, fans spin, one short beep, Ethernet lights off because you pulled the PC out. Restore the display cable and the patch cable before you unbox the spare SODIMM.
