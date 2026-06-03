#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

try:
    import yaml
except ImportError:
    yaml = None

from waike_curriculum.catalog import load_catalog


def main() -> int:
    errors = []
    model = yaml.safe_load((ROOT / "curriculum" / "assessment_model.yaml").read_text()) if yaml else {}
    max_exam = model.get("max_exam_weight", 0.10)
    for course in load_catalog().get("courses", []):
        cid = course["course_id"]
        if course.get("exam_weight_max", 0) > max_exam:
            errors.append(f"{cid}: exam weight too high")
        if not (ROOT / "assessment" / "by_course" / cid / "revision_policy.md").exists():
            errors.append(f"{cid}: no revision policy")
        if not (ROOT / "syllabi" / cid / "portfolio_artifact_requirements.md").exists():
            errors.append(f"{cid}: no portfolio artifact")
    out = ROOT / "results" / "validation" / "no_exam_heavy_report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    status = "PASS" if not errors else "FAIL"
    out.write_text(f"# No exam-heavy report\n\nStatus: {status}\n\n" + "\n".join(f"- {e}" for e in errors) + "\n", encoding="utf-8")
    if errors:
        print("FAIL", errors)
        return 1
    print("PASS validate-no-exam-heavy")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
