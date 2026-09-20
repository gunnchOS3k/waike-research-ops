"""Project owner packages into learner/teacher ingest and product catalog UI schema."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from waike_course_ready.content import COURSES, extra_assessment_items
from waike_course_ready.labs import COURSE_LABS

ROOT = Path(__file__).resolve().parents[2]
KEY_FIELD_NAMES = (
    "answer_index",
    "answer_keys",
    "instructor_keys",
    "solution_key",
    "explanation",
    "correct",
)


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _strip_keys(obj: Any) -> Any:
    if isinstance(obj, dict):
        return {k: _strip_keys(v) for k, v in obj.items() if k not in KEY_FIELD_NAMES}
    if isinstance(obj, list):
        return [_strip_keys(x) for x in obj]
    return obj


def build_learner() -> dict[str, Any]:
    courses = []
    for cid, c in COURSES.items():
        extras = extra_assessment_items(cid)
        quizzes = []
        for w in c["weeks"]:
            quizzes.append(
                {
                    "quiz_id": f"{cid}-q{w['week']:02d}",
                    "week": w["week"],
                    "items": [{"id": i["id"], "kind": i["kind"], "stem": i["stem"], "choices": i["choices"]} for i in w["quiz"]],
                }
            )
        courses.append(
            {
                "course_id": cid,
                "title": c["title"],
                "track_ids": c["track_ids"],
                "academy_id": c["academy_id"],
                "kinesthetic_hook": c["kinesthetic_hook"],
                "lesson_excerpt": c["weeks"][0]["lesson"][:280],
                "worked_example": c["weeks"][0]["worked_example"],
                "assignment": c["weeks"][0]["assignment"],
                "lab_hint": c["weeks"][0]["lab_id"],
                "syllabus": {"weeks": 10, "hook": c["syllabus_hook"]},
                "weeks": [
                    {
                        "week": w["week"],
                        "title": w["title"],
                        "lesson_id": f"{cid}-w{w['week']:02d}",
                        "body_md": w["lesson"],
                        "worked_example": w["worked_example"],
                    }
                    for w in c["weeks"]
                ],
                "assignments": [{"id": f"a{w['week']:02d}", "prompt": w["assignment"]} for w in c["weeks"]],
                "labs": COURSE_LABS[cid],
                "quizzes": quizzes,
                "assessments": {
                    "mid_course": [{"id": i["id"], "stem": i["stem"], "choices": i["choices"]} for i in extras["mid"]],
                    "final_knowledge": [{"id": i["id"], "stem": i["stem"], "choices": i["choices"]} for i in extras["final"]],
                    "practical_labs": COURSE_LABS[cid],
                },
                "portfolio": {"no_pii": True},
                "offline_pack": {
                    "lesson_ids": [f"{cid}-w{w['week']:02d}" for w in c["weeks"]],
                    "session_shape": {
                        "lesson_id": f"{cid}-w01",
                        "role": "learner",
                        "offline_pack": f"{cid}-offline",
                        "labs": COURSE_LABS[cid][:2],
                    },
                },
            }
        )
    doc = {"schema": "waike.learner_ingest.v1", "role": "learner", "generated_utc": _now(), "courses": courses}
    return _strip_keys(doc)


def build_teacher() -> dict[str, Any]:
    learner = build_learner()
    courses = []
    for raw, src in zip(learner["courses"], COURSES.values(), strict=True):
        cid = raw["course_id"]
        extras = extra_assessment_items(cid)
        keys = {
            "quizzes": {
                f"{cid}-q{w['week']:02d}": [
                    {"id": i["id"], "answer_index": i["answer_index"], "explanation": i["explanation"]}
                    for i in w["quiz"]
                ]
                for w in src["weeks"]
            },
            "mid": [{"id": i["id"], "answer_index": i["answer_index"]} for i in extras["mid"]],
            "final": [{"id": i["id"], "answer_index": i["answer_index"]} for i in extras["final"]],
        }
        teacher_course = dict(raw)
        teacher_course["answer_keys"] = keys
        teacher_course["rubrics"] = [f"{cid}-lab", f"{cid}-assignment", f"{cid}-practical", f"{cid}-project"]
        teacher_course["instructor_notes"] = "Keys stay out of learner ingest. Run labs with computing validators."
        teacher_course["presentation"] = [f"week_{w['week']:02d}.md" for w in src["weeks"]]
        courses.append(teacher_course)
    return {
        "schema": "waike.teacher_ingest.v1",
        "role": "educator",
        "generated_utc": _now(),
        "courses": courses,
    }


def build_product_catalog() -> dict[str, Any]:
    """waike.course_catalog.ui.v1 — fields the current WAIKE catalog renderer expects."""
    courses = []
    for cid, c in COURSES.items():
        courses.append(
            {
                "course_id": cid,
                "title": c["title"],
                "kinesthetic_hook": c["kinesthetic_hook"],
                "lesson_excerpt": c["weeks"][0]["lesson"].split("\n\n")[0][:400],
                "worked_example": c["weeks"][0]["worked_example"],
                "assignment": c["weeks"][0]["assignment"],
                "lab_hint": c["weeks"][0]["lab_id"],
                "track_ids": c["track_ids"],
                "academy_id": c["academy_id"],
            }
        )
    return {
        "schema": "waike.course_catalog.ui.v1",
        "full_curriculum_complete": False,
        "owner_repo": "waike-research-ops",
        "packet": "WAIKE-COURSE-READY-002",
        "courses": courses,
    }


CANONICAL_TRACK_IDS: tuple[str, ...] = (
    "DIGITAL_CONFIDENCE",
    "IT_SUPPORT_HARDWARE",
    "SOFTWARE_BUILDER",
    "NETWORKING_INFRA",
    "CYBER_SOC",
    "DATA_DASHBOARDS",
    "AI_ML_EDGE",
    "EMBEDDED_PROTOTYPING",
    "WIRELESS_6G",
    "PM_AGILE_LSS",
    "GAME_DEV_INTERACTIVE",
    "SEVEN_GC_APPRENTICESHIP",
    "CLOUD_DEVOPS",
    "COMM_PD_ETHICS",
    "ROBOTICS_CONTROL",
    "GUNNCHOS_PRODUCT_LAB",
    "HARDWARE_ENGINEERING",
    "DATA_VIZ_BI",
)

# Canonical track_id -> digital_rc package directory (18 tracks / 17 dirs).
TRACK_TO_PACKAGE_DIR: dict[str, str] = {
    "DIGITAL_CONFIDENCE": "GENERAL_IT",
    "IT_SUPPORT_HARDWARE": "GENERAL_IT",
    "SOFTWARE_BUILDER": "SOFTWARE_BUILDER",
    "NETWORKING_INFRA": "COMPUTER_NETWORKING",
    "CYBER_SOC": "CYBERSECURITY",
    "DATA_DASHBOARDS": "DATA_DASHBOARDS",
    "AI_ML_EDGE": "AI_ML_EDGE",
    "EMBEDDED_PROTOTYPING": "EMBEDDED_PROTOTYPING",
    "WIRELESS_6G": "WIRELESS_6G",
    "PM_AGILE_LSS": "PM_AGILE_LSS",
    "GAME_DEV_INTERACTIVE": "GAME_DEV_INTERACTIVE",
    "SEVEN_GC_APPRENTICESHIP": "SEVEN_GC_APPRENTICESHIP",
    "CLOUD_DEVOPS": "CLOUD_DEVOPS",
    "COMM_PD_ETHICS": "COMM_PD_ETHICS",
    "ROBOTICS_CONTROL": "ROBOTICS_CONTROL",
    "GUNNCHOS_PRODUCT_LAB": "GUNNCHOS_PRODUCT_LAB",
    "HARDWARE_ENGINEERING": "HARDWARE_ENGINEERING",
    "DATA_VIZ_BI": "DATA_VIZ_BI",
}


def _course_index_by_package() -> dict[str, dict[str, Any]]:
    """Index authored COURSES plus filesystem digital_rc packages by package dir / course_id."""
    by_id: dict[str, dict[str, Any]] = {}
    for cid, course in COURSES.items():
        by_id[cid] = {"source": "waike_course_ready.content", "course_id": cid, **course}
    digital_rc = ROOT / "curriculum" / "digital_rc"
    if digital_rc.is_dir():
        for course_json in sorted(digital_rc.glob("*/course.json")):
            package_dir = course_json.parent.name
            data = json.loads(course_json.read_text(encoding="utf-8"))
            by_id.setdefault(
                package_dir,
                {
                    "source": "curriculum/digital_rc",
                    "course_id": data.get("course_id", package_dir),
                    "title": data.get("title", package_dir),
                    "track_ids": data.get("track_ids", []),
                    "academy_id": data.get("academy_id"),
                    "package_path": str(course_json.parent.relative_to(ROOT)),
                },
            )
    return by_id


def build_canonical_track_ingest() -> dict[str, Any]:
    """Emit 18 track-keyed ingest entries mapping shared packages where needed.

    Prefer this surface for LP list/open/render by canonical track_id. Package
    directories remain 17 (GENERAL_IT shared by DIGITAL_CONFIDENCE + IT_SUPPORT_HARDWARE).
    """
    packages = _course_index_by_package()
    tracks: list[dict[str, Any]] = []
    for track_id in CANONICAL_TRACK_IDS:
        package_dir = TRACK_TO_PACKAGE_DIR[track_id]
        pkg = packages.get(package_dir)
        canonical_manifest = (
            ROOT / "curriculum" / "canonical_packages" / track_id / "PACKAGE_MANIFEST.v1.json"
        )
        entry: dict[str, Any] = {
            "track_id": track_id,
            "course_id": track_id,
            "package_dir": package_dir,
            "package_course_id": (pkg or {}).get("course_id", package_dir),
            "title": (pkg or {}).get("title") or track_id,
            "academy_id": (pkg or {}).get("academy_id"),
            "digital_rc_path": f"curriculum/digital_rc/{package_dir}",
            "canonical_package_manifest": str(canonical_manifest.relative_to(ROOT)),
            "shared_package": package_dir != track_id,
            "ingest_addressable": pkg is not None and canonical_manifest.is_file(),
            "lp_apis": {
                "list_courses": "GET /api/courses (filter by track_id)",
                "open_course": f"GET /api/courses/{{id}} where id resolves via track_id={track_id}",
                "render_lesson": "GET /api/lessons/{lesson_id} from package weeks",
                "physical_pixel_validation": "OUT_OF_SCOPE",
            },
        }
        if pkg and "weeks" in pkg:
            entry["week_count"] = len(pkg["weeks"])
        tracks.append(entry)
    return {
        "schema": "waike.canonical_track_ingest.v1",
        "role": "platform_ingest_index",
        "generated_utc": _now(),
        "track_count": len(tracks),
        "package_dir_count": len({t["package_dir"] for t in tracks}),
        "tracks": tracks,
    }


def write_ingest() -> dict[str, Path]:
    learner = build_learner()
    teacher = build_teacher()
    catalog = build_product_catalog()
    canonical = build_canonical_track_ingest()
    paths = {
        "learner": ROOT / "ingest" / "learner" / "waike_learner_ingest.v1.json",
        "teacher": ROOT / "ingest" / "teacher" / "waike_teacher_ingest.v1.json",
        "catalog": ROOT / "ingest" / "waike_product_catalog.ui.v1.json",
        "canonical_tracks": ROOT / "ingest" / "canonical" / "waike_canonical_track_ingest.v1.json",
    }
    for p, obj in (
        (paths["learner"], learner),
        (paths["teacher"], teacher),
        (paths["catalog"], catalog),
        (paths["canonical_tracks"], canonical),
    ):
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(obj, indent=2) + "\n", encoding="utf-8")
    return paths
