#!/usr/bin/env python3
"""Fetch open issues via GitHub API (public) or gh; write .audit/open_issues.json."""
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / ".audit"
AUDIT.mkdir(parents=True, exist_ok=True)


def fetch_api():
    url = "https://api.github.com/repos/gunnchOS3k/waike-research-ops/issues?state=open&per_page=100"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode())
    return [
        {
            "number": i["number"],
            "title": i["title"],
            "body": i.get("body", ""),
            "labels": [l["name"] for l in i.get("labels", [])],
            "url": i["html_url"],
            "createdAt": i.get("created_at"),
            "updatedAt": i.get("updated_at"),
        }
        for i in data
        if "pull_request" not in i
    ]


def fetch_gh():
    r = subprocess.run(
        [
            "gh", "issue", "list", "--repo", "gunnchOS3k/waike-research-ops",
            "--state", "open", "--limit", "500",
            "--json", "number,title,body,labels,createdAt,updatedAt,url",
        ],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        return None
    items = json.loads(r.stdout)
    for it in items:
        it["labels"] = [l.get("name", l) if isinstance(l, dict) else l for l in it.get("labels", [])]
    return items


def main() -> int:
    cached = AUDIT / "open_issues.json"
    if cached.exists() and cached.stat().st_size > 100:
        issues = json.loads(cached.read_text())
        print(f"Using cached {len(issues)} issues from .audit/open_issues.json")
    else:
        issues = fetch_gh() or fetch_api()
    (AUDIT / "open_issues.json").write_text(json.dumps(issues, indent=2) + "\n", encoding="utf-8")
    print(f"Fetched {len(issues)} open issues -> .audit/open_issues.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
