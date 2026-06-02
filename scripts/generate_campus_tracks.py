#!/usr/bin/env python3
import argparse, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from waike_ops.reports import write_track_bundle
p = argparse.ArgumentParser()
p.add_argument("--site", required=True)
a = p.parse_args()
write_track_bundle(a.site)
