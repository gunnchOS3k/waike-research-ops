# lab_nif_ipv6_text — IPv6 text form and /48 → /64 subnet count

Write the RFC 5952 canonical form of the full address (lowercase, no leading zeros, :: replaces the first longest zero run of two or more groups) and count /64 subnets in the site prefix.

Submit the change request, then edit one input and confirm the recomputation follows:

python3 scripts/run_course_labs.py --lab lab_nif_ipv6_text --submission path/to/student.json

Common miss: Compressing the second zero run, or using :: for a single zero group, fails.
