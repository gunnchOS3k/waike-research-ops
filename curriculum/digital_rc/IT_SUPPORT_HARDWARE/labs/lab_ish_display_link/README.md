# lab_ish_display_link — Display bandwidth — will the cable carry the mode?

For at least two modes compute width × height × Hz × bpp in Gbit/s and mark fits for HDMI 1.4 (8.16), HDMI 2.0 (14.4), DP 1.4 (25.92). State that ignoring blanking makes this a lower bound.

Grade it on the bench, then alter one part's rating and watch the grader disagree:

python3 scripts/run_course_labs.py --lab lab_ish_display_link --submission path/to/student.json

Common miss: Promising 4K 120 Hz over HDMI 2.0 fails.
