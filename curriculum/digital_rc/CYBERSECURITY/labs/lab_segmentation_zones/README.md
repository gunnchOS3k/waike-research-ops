# lab_segmentation_zones — Kiosk / SOC / guest matrix

kiosk→soc deny. soc→kiosk allow_syslog_only. guest→staff deny.

## Student artifact
Keys: `kiosk_to_soc, soc_to_kiosk, guest_to_staff`.
An empty incident note fails no_attacker_word. targets other than course_ctf_fixture fail no_network.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Harbor SOC repo root, submit fixture answers only. Do not point this lab at a host you do not own.
```
python3 scripts/run_course_labs.py --lab lab_segmentation_zones --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_segmentation_zones --empty
```

Allowing kiosk to SOC is an east-west hole.
