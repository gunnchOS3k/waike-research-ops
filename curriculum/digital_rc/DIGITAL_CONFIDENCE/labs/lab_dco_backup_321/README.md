# lab_dco_backup_321 — Backups — three copies, two media, one offsite, one tested restore

List every copy with media type and offsite flag, evaluate each 3-2-1 rule, and set plan_ok only if a restore was tested.

Try it, then change one number in your file and check that the answer moves:

python3 scripts/run_course_labs.py --lab lab_dco_backup_321 --submission path/to/student.json

Common miss: Calling two copies on one drive a backup plan fails.
