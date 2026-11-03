# lab_soc_log_parse — Auth log anatomy — failures per source and the success that follows

Parse the eight-line sshd fixture. Report failed_by_ip counts, the top_source, and accepted_after_failures (addresses that logged in after failing).

Run it at the desk, then swap one log line and confirm the verdict changes:

python3 scripts/run_course_labs.py --lab lab_soc_log_parse --submission path/to/student.json

Common miss: Counting the Accepted line as a failure, or missing the root success from 203.0.113.45, fails.
