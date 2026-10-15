"""Bounded local CSV/SQLite worked example; no network or learner-code execution.

Evidence is computed from source bytes. It is practice, not an LMS grade.
"""
import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
import math
from pathlib import Path
import sqlite3

VERSION = 'pier-ledger/1.0.0-review'
HEADER = ['visit_id', 'pier_bay', 'ts_utc', 'headcount', 'source_file']
ALIASES = {'Bay-A': 'bay_a', 'bay_a': 'bay_a', 'BAY A': 'bay_a', 'Bay-B': 'bay_b', 'bay_b': 'bay_b'}
DEFAULT_META = [('bay_a', 'North pier'), ('bay_b', 'South pier')]


def aware_time(value):
    if not isinstance(value, str):
        raise ValueError('timestamp must be text with an explicit timezone')
    try:
        time = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as error:
        raise ValueError('invalid timestamp') from error
    if time.tzinfo is None:
        raise ValueError('explicit timezone required')
    return time.astimezone(timezone.utc)


def inspect(raw):
    if not isinstance(raw, bytes) or not raw or len(raw) > 65536:
        raise ValueError('a nonempty CSV of at most 65536 bytes is required')
    try:
        reader = csv.DictReader(io.StringIO(raw.decode('utf-8-sig'), newline=''), strict=True)
        if reader.fieldnames != HEADER:
            raise ValueError('schema must exactly match the five documented columns in order')
        rows = list(reader)
    except (UnicodeError, csv.Error) as error:
        raise ValueError('CSV must be valid UTF-8 with valid quoting') from error
    if not rows or len(rows) > 1000:
        raise ValueError('expected 1..1000 rows')
    seen, cleaned, rejected = set(), [], []
    missing = 0
    for row in rows:
        if None in row or any(v is None for v in row.values()):
            raise ValueError('row width does not match schema')
        visit = row['visit_id']
        if not visit or visit in seen:
            raise ValueError('visit_id must be nonempty and unique; do not silently deduplicate')
        seen.add(visit)
        if row['pier_bay'] not in ALIASES:
            raise ValueError('unknown pier alias; revise the documented mapping before analysis')
        when = aware_time(row['ts_utc']).isoformat()
        if not row['source_file']:
            raise ValueError('source_file cannot be empty')
        value = row['headcount']
        if value == '':
            missing += 1
            rejected.append({'visit_id': visit, 'reason': 'missing_headcount'})
            continue
        try:
            number = int(value)
        except ValueError as error:
            raise ValueError('headcount must be an integer or an empty missing cell') from error
        if number < 0:
            rejected.append({'visit_id': visit, 'reason': 'negative_headcount'})
            continue
        if number > 1000000:
            raise ValueError('headcount exceeds this teaching model limit')
        cleaned.append((visit, ALIASES[row['pier_bay']], when, number))
    return rows, cleaned, rejected, missing


def analyze(raw, *, threshold=40, metadata=None, now='2026-10-01T18:40:00Z', sla_minutes=30):
    if type(threshold) is not int or not 0 <= threshold <= 1000000:
        raise ValueError('threshold must be an integer from 0 to 1000000')
    if type(sla_minutes) is not int or not 0 <= sla_minutes <= 10080:
        raise ValueError('sla_minutes must be an integer from 0 to 10080')
    now_time = aware_time(now)
    rows, cleaned, rejected, missing = inspect(raw)
    metadata = DEFAULT_META if metadata is None else metadata
    if not isinstance(metadata, list) or not metadata:
        raise ValueError('nonempty metadata list required')
    keys = []
    for record in metadata:
        if not isinstance(record, (list, tuple)) or len(record) != 2 or not all(isinstance(v, str) and v for v in record):
            raise ValueError('metadata rows must contain a key and a display label')
        keys.append(record[0])
    if len(keys) != len(set(keys)):
        raise ValueError('duplicate metadata keys would multiply joined rows')
    if not cleaned:
        raise ValueError('no valid headcounts remain; no ordinary KPI can be reported')
    newest = max(aware_time(row[2]) for row in cleaned)
    if newest > now_time:
        raise ValueError('fixture contains a future observation; inspect clock assumptions')
    with sqlite3.connect(':memory:') as db:
        db.execute('CREATE TABLE pier_visits (visit_id TEXT PRIMARY KEY, pier_bay TEXT NOT NULL, ts_utc TEXT NOT NULL, headcount INTEGER NOT NULL CHECK(headcount >= 0))')
        db.executemany('INSERT INTO pier_visits VALUES (?, ?, ?, ?)', cleaned)
        db.execute('CREATE TABLE pier_meta (pier_bay TEXT PRIMARY KEY, label TEXT NOT NULL)')
        db.executemany('INSERT INTO pier_meta VALUES (?, ?)', metadata)
        # Bound values are data. The exercise never accepts SQL submitted by a remote visitor.
        selected = db.execute('SELECT visit_id, headcount FROM pier_visits WHERE headcount > ? ORDER BY visit_id', (threshold,)).fetchall()
        groups = db.execute('SELECT pier_bay, COUNT(*), AVG(headcount) FROM pier_visits GROUP BY pier_bay ORDER BY pier_bay').fetchall()
        orphans = db.execute('SELECT v.visit_id FROM pier_visits v LEFT JOIN pier_meta m ON v.pier_bay=m.pier_bay WHERE m.pier_bay IS NULL ORDER BY v.visit_id').fetchall()
        joined = db.execute('SELECT COUNT(*) FROM pier_visits v INNER JOIN pier_meta m ON v.pier_bay=m.pier_bay').fetchone()[0]
    values = sorted(row[3] for row in cleaned)
    age = (now_time - newest).total_seconds() / 60
    return {
        'version': VERSION, 'evidence_type': 'computed_local_practice',
        'source_sha256': hashlib.sha256(raw).hexdigest(),
        'columns': HEADER, 'rows_in': len(rows), 'rows_out': len(cleaned),
        'rejected': rejected, 'missing_rate_raw': missing / len(rows),
        'threshold': threshold, 'selected_rows': [list(r) for r in selected],
        'group_summary': [{'pier_bay': b, 'n': n, 'mean_headcount': m} for b, n, m in groups],
        'mean_headcount': sum(values) / len(values),
        'p95_nearest_rank': values[math.ceil(0.95 * len(values)) - 1],
        'join': {'inner_rows': joined, 'orphan_ids': [r[0] for r in orphans]},
        'freshness': {'as_of': now_time.isoformat(), 'newest_valid_observation': newest.isoformat(), 'age_minutes': age, 'sla_minutes': sla_minutes, 'within_policy': age <= sla_minutes},
        'claim_boundary': 'Original fictional counts; no real visitors, operational SLA or causal effect measured.',
        'competency_demonstrated': False, 'instructor_review': 'pending',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--threshold', type=int, default=40)
    parser.add_argument('--now', default='2026-10-01T18:40:00Z')
    args = parser.parse_args()
    try:
        # Read a bounded amount even when the input file is unexpectedly large.
        with args.input.open('rb') as stream:
            raw = stream.read(65537)
        result = analyze(raw, threshold=args.threshold, now=args.now)
        with args.output.open('x', encoding='utf-8') as stream:
            json.dump(result, stream, indent=2, allow_nan=False)
            stream.write('\n')
    except (ValueError, OSError) as error:
        parser.exit(2, f'Input/output rejected: {error}\n')
    print(f'Computed practice evidence saved: {args.output.name}; instructor review pending')


if __name__ == '__main__':
    main()
