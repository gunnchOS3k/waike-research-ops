# lab_nif_bgp_path — BGP best path — local preference before path length

Run the simplified decision order (highest local_pref, shortest AS_PATH, lowest origin, lowest MED, lowest router ID) on R1–R3. Report the winner and the attribute that removed the last competitor.

Submit the change request, then edit one input and confirm the recomputation follows:

python3 scripts/run_course_labs.py --lab lab_nif_bgp_path --submission path/to/student.json

Common miss: Picking the shortest AS_PATH first ignores local preference.
