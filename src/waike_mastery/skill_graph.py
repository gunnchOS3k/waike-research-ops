"""Prerequisite / skill graph derived from discoverable course weeks — privacy-safe labels."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .discover import discover_courses

ROOT = Path(__file__).resolve().parents[2]


def build_skill_graph(root: Path | None = None) -> dict[str, Any]:
    root = root or ROOT
    courses = discover_courses(root)
    nodes: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []

    for meta in courses:
        cid = meta["course_id"]
        course_node = f"course:{cid}"
        nodes.append(
            {
                "id": course_node,
                "kind": "course",
                "label": meta["title"],
                "privacy_safe": True,
            }
        )
        prev_week = None
        for week_n in range(1, (meta.get("weeks") or 0) + 1):
            skill_id = f"skill:{cid}:w{week_n:02d}"
            nodes.append(
                {
                    "id": skill_id,
                    "kind": "weekly_skill",
                    "course_id": cid,
                    "week": week_n,
                    "label": f"{cid} week {week_n} practice",
                    # Never demeaning learner labels — skills are content nodes only.
                    "learner_label_policy": "skill_focus_only",
                }
            )
            edges.append({"from": course_node, "to": skill_id, "relation": "includes"})
            if prev_week:
                edges.append({"from": prev_week, "to": skill_id, "relation": "prerequisite"})
            prev_week = skill_id
        # labs hang off mid-course skills
        for i, lab_id in enumerate(meta.get("lab_ids") or []):
            lab_node = f"lab:{cid}:{lab_id}"
            nodes.append(
                {
                    "id": lab_node,
                    "kind": "lab_skill",
                    "course_id": cid,
                    "label": lab_id,
                    "learner_label_policy": "skill_focus_only",
                }
            )
            anchor_week = min(i + 1, meta.get("weeks") or 1)
            edges.append(
                {
                    "from": f"skill:{cid}:w{anchor_week:02d}",
                    "to": lab_node,
                    "relation": "assesses",
                }
            )

    return {
        "schema": "waike.mastery_skill_graph.v1",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "node_count": len(nodes),
        "edge_count": len(edges),
        "forbidden_learner_labels": [
            "dumb",
            "slow",
            "hopeless",
            "bad_student",
            "low_iq",
            "lazy",
        ],
        "nodes": nodes,
        "edges": edges,
    }
