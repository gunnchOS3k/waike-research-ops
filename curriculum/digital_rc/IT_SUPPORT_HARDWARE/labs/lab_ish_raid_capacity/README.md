# lab_ish_raid_capacity — RAID usable capacity and guaranteed failures

For your array (≥4 disks), give usable TB and guaranteed tolerated failures for RAID 0, 1, 5, 6, 10. raid_is_backup must be false.

Grade it on the bench, then alter one part's rating and watch the grader disagree:

python3 scripts/run_course_labs.py --lab lab_ish_raid_capacity --submission path/to/student.json

Common miss: Counting parity disks as usable space, or calling RAID a backup, fails.
