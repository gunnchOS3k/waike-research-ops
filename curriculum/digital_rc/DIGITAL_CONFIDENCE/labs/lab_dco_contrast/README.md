# lab_dco_contrast — Readable screens — WCAG contrast ratio

For at least two colour pairs compute the WCAG 2.2 contrast ratio and report aa_normal (≥ 4.5) and aa_large (≥ 3.0).

Try it, then change one number in your file and check that the answer moves:

python3 scripts/run_course_labs.py --lab lab_dco_contrast --submission path/to/student.json

Common miss: Eyeballing #777777 on white as passing AA normal text fails; it is 4.48:1.
