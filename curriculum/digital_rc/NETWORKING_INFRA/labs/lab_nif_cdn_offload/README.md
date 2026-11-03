# lab_nif_cdn_offload — CDN offload — what the origin still sees

For at least two request hit ratios, compute origin requests per second and origin Gbit/s from the total rate and the average object size.

Submit the change request, then edit one input and confirm the recomputation follows:

python3 scripts/run_course_labs.py --lab lab_nif_cdn_offload --submission path/to/student.json

Common miss: Multiplying by the hit ratio instead of the miss ratio fails.
