# lab_wifi_fundamentals — Wi-Fi fundamentals on Packet Range fixture

Map SSID/band/channel/auth for the authorized Packet Range guest SSID. No live campus survey claims.

## Student artifact
Keys: `ssid, band_ghz, channel, auth, guest_isolated`.
Missing parse fields fail. A TTL story of `(1-1)==0` without a header byte fails.
A file whose entire body is `PASS` is rejected by `_fail_if_print_pass`.

## How to run
From the Packet Range repo root, submit the parse/table JSON you computed. A GUI screenshot is not a validator input.
```
python3 scripts/run_course_labs.py --lab lab_wifi_fundamentals --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_wifi_fundamentals --empty
```

Wrong auth or guest_isolated=false fails isolation check.
