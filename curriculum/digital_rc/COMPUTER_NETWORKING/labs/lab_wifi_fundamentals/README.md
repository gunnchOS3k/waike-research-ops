# lab_wifi_fundamentals — Wi-Fi fundamentals on Packet Range guest SSID

Configure a guest SSID plan: band, channel, WPA3 (or lab-only OPEN), guest isolation true. No unauthorized RF transmit claims.

## Student artifact
Keys: `ssid, band_ghz, channel, auth, guest_isolated`.
Empty {} fails. A file whose entire body is PASS raises _fail_if_print_pass.

## How to run
```
python3 scripts/run_course_labs.py --lab lab_wifi_fundamentals --submission path/to/student.json
python3 scripts/run_course_labs.py --lab lab_wifi_fundamentals --empty
```

