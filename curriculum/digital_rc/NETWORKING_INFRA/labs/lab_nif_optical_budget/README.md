# lab_nif_optical_budget — Optical link budget — loss, margin, 3 dB rule

Planning coefficients: 0.35 dB/km, 0.5 dB per connector, 0.1 dB per splice. Margin = tx − loss − receiver sensitivity; the span passes at ≥ 3 dB.

Submit the change request, then edit one input and confirm the recomputation follows:

python3 scripts/run_course_labs.py --lab lab_nif_optical_budget --submission path/to/student.json

Common miss: Counting only fiber loss and ignoring connectors overstates margin.
