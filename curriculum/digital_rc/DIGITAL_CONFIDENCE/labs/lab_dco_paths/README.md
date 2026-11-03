# lab_dco_paths — Folders and paths — where does ../ actually land?

For at least two tasks give cwd (absolute), a relative path, and the absolute path it resolves to. At least one relative path must climb with ..

Try it, then change one number in your file and check that the answer moves:

python3 scripts/run_course_labs.py --lab lab_dco_paths --submission path/to/student.json

Common miss: A cwd that is not absolute, or forgetting that .. cancels the folder before it, fails.
