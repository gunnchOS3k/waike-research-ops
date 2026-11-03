# lab_ish_partition_scheme — MBR or GPT — the 2^32-sector ceiling

Compute the MBR limit 2^32 × sector size, pick GPT when the disk is larger, and boot GPT system disks with UEFI.

Grade it on the bench, then alter one part's rating and watch the grader disagree:

python3 scripts/run_course_labs.py --lab lab_ish_partition_scheme --submission path/to/student.json

Common miss: Formatting a 4 TB disk as MBR strands the space above 2 TiB.
