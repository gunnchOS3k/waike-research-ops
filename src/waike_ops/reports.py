import json
from pathlib import Path
from .campus_tracks import list_sites, load_track


def write_track_bundle(site_id: str) -> None:
    t = load_track(site_id)
    out = Path("results/campus_learning")
    out.mkdir(parents=True, exist_ok=True)
    (out / f"{site_id}_learning_track.md").write_text(
        f"# Learning track — {site_id}\n\n```json\n{json.dumps(t, indent=2)}\n```\n", encoding="utf-8"
    )
    (out / f"{site_id}_apprenticeship_path.md").write_text(f"# Apprenticeship — {site_id}\n\nAdvanced path repos: {t['advanced_pathway']['repos']}\n", encoding="utf-8")
    (out / f"{site_id}_family_learning_night.md").write_text(f"# Family night — {site_id}\n\n{t['family_community_activity']}\n", encoding="utf-8")
    (out / f"{site_id}_instructor_packet.md").write_text(f"# Instructor packet\n\nRole: {t['instructor_role']}\n", encoding="utf-8")
    (out / f"{site_id}_capstone_brief.md").write_text(f"# Capstone\n\n{t['local_capstone']}\n", encoding="utf-8")


def write_all() -> None:
    for s in list_sites():
        write_track_bundle(s)
