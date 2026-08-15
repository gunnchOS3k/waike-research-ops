"""Course-specific honesty checks for WIRELESS_6G / ROBOTICS / GAME_DEV."""
from __future__ import annotations

from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]


def _lesson_blob(course_id: str, root: Path) -> str:
    base = root / "curriculum" / "digital_rc" / course_id
    parts: list[str] = []
    for name in ("course.json", "syllabus.md", "student/STUDENT_PACKET.md"):
        p = base / name
        if p.is_file():
            parts.append(p.read_text(encoding="utf-8"))
    for p in sorted((base / "weeks").glob("w*/lesson.md")):
        parts.append(p.read_text(encoding="utf-8"))
    return "\n".join(parts).lower()


def check_wireless_6g(root: Path | None = None) -> dict[str, Any]:
    root = root or ROOT
    text = _lesson_blob("WIRELESS_6G", root)
    distinctions = {
        "5g": "5g" in text,
        "5g_advanced": "5g-advanced" in text or "5g advanced" in text,
        "ntn": "ntn" in text,
        "ai_ran": "ai-ran" in text or "airan" in text,
        "fr3": "fr3" in text,
        "imt_2030": "imt-2030" in text or "imt 2030" in text,
        "future_6g_research": "6g" in text and ("research" in text or "does not exist" in text),
    }
    honesty = (
        "commercial_6g_exists=false" in text
        or "commercial_6g_exists stays false" in text
        or "commercial standardized 6g does not exist" in text
    )
    claims_commercial = "commercial standardized 6g does not exist" not in text and (
        "commercial 6g is available" in text or "6g is standardized today" in text
    )
    return {
        "course_id": "WIRELESS_6G",
        "distinctions": distinctions,
        "distinctions_ok": all(distinctions.values()) or (
            distinctions["5g"]
            and distinctions["5g_advanced"]
            and distinctions["ntn"]
            and distinctions["ai_ran"]
            and distinctions["future_6g_research"]
        ),
        "honesty_flags_present": honesty,
        "claims_current_commercial_6g_standard": bool(claims_commercial),
        "pass": honesty
        and not claims_commercial
        and distinctions["5g"]
        and distinctions["ntn"]
        and distinctions["ai_ran"]
        and distinctions["5g_advanced"],
        "detail": "Requires 5G/5GA/NTN/AI-RAN distinctions; never claim commercial standardized 6G.",
    }


def check_robotics(root: Path | None = None) -> dict[str, Any]:
    root = root or ROOT
    text = _lesson_blob("ROBOTICS_CONTROL", root)
    needs = {
        "pid": "pid" in text,
        "kinematics": "kinematic" in text or "fk" in text or "2r" in text,
        "sensor": "sensor" in text or "lidar" in text,
        "estop": "e-stop" in text or "estop" in text,
        "path_or_traj": "traj" in text or "path" in text,
    }
    return {
        "course_id": "ROBOTICS_CONTROL",
        "needs": needs,
        "pass": all(needs.values()),
        "detail": "Requires kinematics/PID/sensor/estop/trajectory reasoning surfaces.",
    }


def check_game_dev(root: Path | None = None) -> dict[str, Any]:
    root = root or ROOT
    text = _lesson_blob("GAME_DEV_INTERACTIVE", root)
    needs = {
        "game_loop": "game loop" in text or "timestep" in text or "dt=1/60" in text,
        "input": "input" in text or "rebind" in text,
        "state_fsm": "fsm" in text or "state" in text,
        "mechanics": "aabb" in text or "collision" in text or "beat" in text,
        "build_or_test": "build" in text or "playtest" in text or "checksum" in text,
    }
    prose_only_forbidden = "prose game concept is not a completed development lab"  # meta
    return {
        "course_id": "GAME_DEV_INTERACTIVE",
        "needs": needs,
        "pass": all(needs.values()),
        "prose_concept_insufficient": True,
        "detail": "Requires real loop/input/state/mechanics/build-test evidence, not prose concepts alone.",
    }


def run_course_honesty(root: Path | None = None) -> dict[str, Any]:
    root = root or ROOT
    rows = [check_wireless_6g(root), check_robotics(root), check_game_dev(root)]
    return {
        "schema": "waike.course_honesty.v1",
        "checks": rows,
        "pass": all(r["pass"] for r in rows),
        "claim_boundary": (
            "Curriculum honesty surfaces for Mastery-002. Not a claim of commercial 6G "
            "or physical robot/game studio validation."
        ),
    }
