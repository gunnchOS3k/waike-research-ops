# lab_soc_attack_map — ATT&CK mapping — behaviours to technique IDs and tactics

Map behaviours B1–B5 to their MITRE ATT&CK technique ID and one valid tactic. actor_attribution_claim must be false.

Run it at the desk, then swap one log line and confirm the verdict changes:

python3 scripts/run_course_labs.py --lab lab_soc_attack_map --submission path/to/student.json

Common miss: Naming a threat group from technique overlap alone fails.
