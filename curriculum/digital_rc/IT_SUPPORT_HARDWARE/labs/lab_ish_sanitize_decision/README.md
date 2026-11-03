# lab_ish_sanitize_decision — Media sanitization — Clear, Purge, or Destroy

Apply the bench rule (inspired by NIST SP 800-88): failed media → Destroy; leaving the organisation → Purge; internal reuse → Clear. Record verification and a certificate ID.

Grade it on the bench, then alter one part's rating and watch the grader disagree:

python3 scripts/run_course_labs.py --lab lab_ish_sanitize_decision --submission path/to/student.json

Common miss: A quick format on a donated SSD is not Purge.
