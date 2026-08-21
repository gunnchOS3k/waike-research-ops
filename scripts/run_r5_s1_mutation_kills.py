#!/usr/bin/env python3
"""Disposable mutation kill harness for WAIKE R5-S1 (mutated files never committed)."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ART = ROOT / "artifacts" / "code_health_r5_s1" / "waike"


def flip_return_zero(text: str) -> str:
    return re.sub(r"return\s+0\b", "return 1", text, count=1)


def remove_validation(text: str) -> str:
    m = re.search(r"\n(\s+)raise\s+(ValueError|ValidationError|AssertionError)\b[^\n]*\n", text)
    if not m:
        raise RuntimeError("remove_validation: no raise found")
    return text[: m.start()] + "\n" + m.group(1) + "pass  # CHAB_REMOVED_VALIDATION\n" + text[m.end() :]


def invert_condition(text: str) -> str:
    m = re.search(r"if\s+(.+?)\s*==\s*(.+?):", text)
    if not m:
        raise RuntimeError("invert_condition: no == found")
    return text[: m.start()] + f"if {m.group(1)} != {m.group(2)}:" + text[m.end() :]


CASES = [
    ("src/waike_curriculum/evaluation/metrics.py", "flip_return_zero", flip_return_zero, "MUTATION_KILLED"),
    ("src/waike_course_ready/batch002/exams.py", "remove_validation", remove_validation, "MUTATION_KILLED"),
    ("src/waike_course_ready/batch002/labs.py", "invert_condition", invert_condition, "MUTATION_KILLED"),
]


def copy_repo(dst: Path) -> None:
    ignore = shutil.ignore_patterns(
        ".git",
        ".tmp_*",
        "artifacts",
        "node_modules",
        ".pytest_cache",
        "__pycache__",
        ".worktrees",
        "*.pyc",
    )
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(ROOT, dst, symlinks=True, ignore=ignore)


def run_make_test(cwd: Path) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    env["PYTHONPATH"] = str(cwd / "src") + (":" + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
    return subprocess.run(
        ["make", "test"],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        timeout=420,
        env=env,
    )


def main() -> int:
    ART.mkdir(parents=True, exist_ok=True)
    base = Path(tempfile.mkdtemp(prefix="waike_r5s1_mut_"))
    results = []
    ok = True
    try:
        clean = base / "clean"
        copy_repo(clean)
        base_run = run_make_test(clean)
        if base_run.returncode != 0:
            print("baseline make test failed", file=sys.stderr)
            print(base_run.stdout[-1000:], file=sys.stderr)
            print(base_run.stderr[-1000:], file=sys.stderr)
            return 2

        for rel, kind, apply_fn, expected in CASES:
            wt = base / kind
            copy_repo(wt)
            path = wt / rel
            original = path.read_text(encoding="utf-8")
            mutated = apply_fn(original)
            if mutated == original:
                print(f"mutation did not apply: {rel} {kind}", file=sys.stderr)
                return 3
            path.write_text(mutated, encoding="utf-8")
            run = run_make_test(wt)
            outcome = "MUTATION_KILLED" if run.returncode != 0 else "MUTATION_SURVIVED"
            entry = {
                "path": rel,
                "kind": kind,
                "mutated_returncode": run.returncode,
                "mutation_outcome": outcome,
                "expected_outcome": expected,
            }
            results.append(entry)
            if outcome != expected:
                ok = False

        payload = {
            "repository": "waike-research-ops",
            "MUTATED_FILES_COMMITTED": False,
            "baseline_pass": True,
            "mutations": results,
            "WAIKE_METRICS_MUTATION_KILLED": any(
                r["path"].endswith("metrics.py") and r["mutation_outcome"] == "MUTATION_KILLED" for r in results
            ),
            "WAIKE_EXAM_MUTATION_KILLED": any(
                r["path"].endswith("exams.py") and r["mutation_outcome"] == "MUTATION_KILLED" for r in results
            ),
            "WAIKE_EXISTING_LABS_MUTATION_STILL_KILLED": any(
                r["path"].endswith("labs.py") and r["mutation_outcome"] == "MUTATION_KILLED" for r in results
            ),
        }
        (ART / "MUTATION_REGRESSION_RESULT.json").write_text(json.dumps(payload, indent=2) + "\n")
        print(json.dumps(payload, indent=2))
        return 0 if ok else 1
    finally:
        shutil.rmtree(base, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
