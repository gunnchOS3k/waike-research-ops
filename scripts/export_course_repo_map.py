#!/usr/bin/env python3
"""Export WAIKE course → repo mapping for supervisors."""
from pathlib import Path

MAP = """# WAIKE Course → Repo Map

| Course | Primary repo |
|--------|--------------|
| 7GC AI-RAN Apprenticeship | 7gc-digital-twin |
| Wireless 6G Foundations | readygary-6g-beam-selection |
| Edge Measurement | edge-io-measurement-node |
| NTN Resilience | ntn-resilience-sim |
| AI-RAN Gary | spectrumx-ai-ran-gary |
"""

def main() -> None:
    out = Path("docs/generated/course_repo_map.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(MAP)
    print(MAP)


if __name__ == "__main__":
    main()
