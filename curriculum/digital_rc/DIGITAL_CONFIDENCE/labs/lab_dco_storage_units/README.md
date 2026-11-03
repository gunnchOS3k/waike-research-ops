# lab_dco_storage_units — Storage units — the 500 GB drive that shows 465 GiB

Convert the box size to GiB, total the photo folder in GiB (MB = 10^6 bytes), and decide whether it fits in the free GiB.

Try it, then change one number in your file and check that the answer moves:

python3 scripts/run_course_labs.py --lab lab_dco_storage_units --submission path/to/student.json

Common miss: Mixing decimal GB with binary GiB makes the photos look like they fit; they do not.
