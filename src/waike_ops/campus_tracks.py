from pathlib import Path
import yaml

DIR = Path(__file__).resolve().parents[2] / "configs" / "campus_learning_tracks"


def list_sites() -> list[str]:
    return sorted(p.stem for p in DIR.glob("*.yaml"))


def load_track(site_id: str) -> dict:
    with (DIR / f"{site_id}.yaml").open(encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data
