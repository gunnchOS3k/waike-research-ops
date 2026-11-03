# lab_dco_attachment_fit — Attachments — base64 growth against the mail limit

Compute the encoded size 4·ceil(bytes/3), compare it with the limit, and choose attach or share_link.

Try it, then change one number in your file and check that the answer moves:

python3 scripts/run_course_labs.py --lab lab_dco_attachment_fit --submission path/to/student.json

Common miss: Comparing the raw file size with the limit fails for files near the edge.
