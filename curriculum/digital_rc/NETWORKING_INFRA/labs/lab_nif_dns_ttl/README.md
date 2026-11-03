# lab_nif_dns_ttl — DNS TTL — how long a change stays invisible

From TTL, the time a resolver cached the record, and the change time, compute when the cache expires, the stale window, the worst case, and the latest time to lower the TTL beforehand.

Submit the change request, then edit one input and confirm the recomputation follows:

python3 scripts/run_course_labs.py --lab lab_nif_dns_ttl --submission path/to/student.json

Common miss: Assuming a change is visible the moment the zone is edited fails.
