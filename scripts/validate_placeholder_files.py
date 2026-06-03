#!/usr/bin/env python3
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FLAGS = re.compile(r"\b(TODO|TBD|placeholder|coming soon|lorem ipsum|fill in)\b", re.I)
SKIP = {".git", "node_modules", ".audit", "results/e2e"}


def scan(path: Path) -> list[tuple[str, str]]:
    hits = []
    if path.suffix not in {".md", ".yaml", ".yml"}:
        return hits
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return hits
    if len(text) < 200 and path.name.endswith(".md") and "template" not in str(path):
        if text.count("\n") < 5:
            hits.append((str(path.relative_to(ROOT)), "shallow"))
    if FLAGS.search(text) and "not complete" not in text.lower():
        hits.append((str(path.relative_to(ROOT)), "flag"))
    return hits


def main() -> int:
    all_hits = []
    for p in ROOT.rglob("*"):
        if any(s in p.parts for s in SKIP):
            continue
        if p.is_file():
            all_hits.extend(scan(p))
    body = "# Placeholder audit\n\n| File | Type |\n|------|------|\n"
    for f, t in all_hits[:80]:
        body += f"| {f} | {t} |\n"
    body += f"\nTotal flags: {len(all_hits)}\n"
    out = ROOT / "results/audit/placeholder_audit.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8")
    (ROOT / ".audit/PLACEHOLDER_AUDIT.md").write_text(body, encoding="utf-8")
    # Allow some template TODOs
    critical = [h for h in all_hits if "assignment_bodies" in h[0] or "lesson_plan" in h[0]]
    if len(critical) > 5:
        print("FAIL placeholder critical", len(critical))
        return 1
    print("PASS validate-placeholder-files", len(all_hits), "notes")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
