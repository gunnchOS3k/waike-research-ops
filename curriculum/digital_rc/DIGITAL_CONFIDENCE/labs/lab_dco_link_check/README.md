# lab_dco_link_check — Reading a link — hostname, registered domain, decision

Pull the hostname out of the URL, read the registered domain from the right (last two labels for these example links), and decide safe_to_open against the expected domain.

Try it, then change one number in your file and check that the answer moves:

python3 scripts/run_course_labs.py --lab lab_dco_link_check --submission path/to/student.json

Common miss: Trusting the familiar word at the left of the hostname fails.
