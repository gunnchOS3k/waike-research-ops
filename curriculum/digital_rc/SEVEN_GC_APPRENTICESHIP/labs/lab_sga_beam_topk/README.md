# lab_sga_beam_topk — Beam selection top-k accuracy on the 8-sample fixture

true_beams = [3,7,1,4,4,0,6,2]; ranked = [[3,2,5],[6,7,1],[1,0,2],[5,6,4],[4,3,5],[2,1,3],[6,5,7],[0,1,2]]. Report top1, top3, n_samples, dataset_class.

The grader recomputes every number from your inputs; an empty object or a bare PASS string is refused.

python3 scripts/run_course_labs.py --lab lab_sga_beam_topk --submission path/to/student.json

Common miss: Counting a top-3 hit as top-1, or labeling the fixture MEASURED, fails.
