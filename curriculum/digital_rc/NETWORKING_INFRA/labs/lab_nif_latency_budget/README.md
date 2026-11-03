# lab_nif_latency_budget — Fiber latency budget — propagation plus serialization

Light in fiber travels at c / 1.468. Compute propagation ms for the route, serialization ms for one packet on the link, and their one-way sum.

Submit the change request, then edit one input and confirm the recomputation follows:

python3 scripts/run_course_labs.py --lab lab_nif_latency_budget --submission path/to/student.json

Common miss: Using the vacuum speed of light under-states fiber delay by about a third.
