# lab_sga_paired_ci — Paired 95% interval — baseline vs model over five seeds

baseline = [0.61,0.63,0.60,0.62,0.64], model = [0.66,0.65,0.67,0.64,0.68]. Use the paired t-interval with t(0.975, df=4) = 2.776. Claim improvement only if the interval excludes 0.

The grader recomputes every number from your inputs; an empty object or a bare PASS string is refused.

python3 scripts/run_course_labs.py --lab lab_sga_paired_ci --submission path/to/student.json

Common miss: Using a z-value, unpaired variance, or claiming improvement against the interval fails.
