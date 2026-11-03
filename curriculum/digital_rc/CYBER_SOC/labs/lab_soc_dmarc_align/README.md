# lab_soc_dmarc_align — Email authentication — SPF/DKIM pass versus DMARC alignment

For messages A and B report spf_aligned, dkim_aligned, and dmarc_pass using relaxed alignment on the organisational domain.

Run it at the desk, then swap one log line and confirm the verdict changes:

python3 scripts/run_course_labs.py --lab lab_soc_dmarc_align --submission path/to/student.json

Common miss: Treating 'SPF pass' as 'DMARC pass' for message B fails.
