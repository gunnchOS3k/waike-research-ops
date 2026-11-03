# lab_nif_p95_billing — 95th-percentile transit billing

Sort the five-minute samples, discard the top 5% (index ceil(0.95·n) − 1 is billed), and multiply by the price per Mbit/s.

Submit the change request, then edit one input and confirm the recomputation follows:

python3 scripts/run_course_labs.py --lab lab_nif_p95_billing --submission path/to/student.json

Common miss: Billing the peak or the mean fails.
