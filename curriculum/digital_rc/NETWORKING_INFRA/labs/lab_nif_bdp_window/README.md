# lab_nif_bdp_window — Bandwidth-delay product and the 64 KiB window ceiling

Compute BDP bytes = rate × RTT / 8, the throughput a fixed window allows (window × 8 / RTT), and the RFC 7323 window-scale shift needed to cover the BDP.

Submit the change request, then edit one input and confirm the recomputation follows:

python3 scripts/run_course_labs.py --lab lab_nif_bdp_window --submission path/to/student.json

Common miss: Forgetting to convert ms to seconds or bits to bytes fails.
