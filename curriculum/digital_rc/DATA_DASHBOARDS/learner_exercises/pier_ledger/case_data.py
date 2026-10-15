"""Original fictional teaching data. No real people or operational telemetry."""
import argparse
import csv
import io
from pathlib import Path
import random

HEADER = ['visit_id', 'pier_bay', 'ts_utc', 'headcount', 'source_file']
PRACTICE = b'''visit_id,pier_bay,ts_utc,headcount,source_file
v1,Bay-A,2026-10-01T18:00:00Z,20,fictional.csv
v2,bay_a,2026-10-01T18:05:00Z,40,fictional.csv
v3,BAY A,2026-10-01T18:10:00Z,60,fictional.csv
v4,Bay-B,2026-10-01T18:15:00Z,80,fictional.csv
v5,bay_b,2026-10-01T18:20:00Z,,fictional.csv
v6,Bay-B,2026-10-01T18:25:00Z,-2,fictional.csv
'''


def independent(seed):
    """Fresh deterministic input, not a completed independent assessment."""
    if type(seed) is not int or not 0 <= seed <= 999999:
        raise ValueError('seed must be an integer from 0 to 999999')
    rng = random.Random(seed)
    output = io.StringIO(newline='')
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(HEADER)
    for i in range(1, 13):
        label = rng.choice(['Bay-A', 'bay_a', 'BAY A', 'Bay-B', 'bay_b'])
        value = '' if i == 5 else (-1 if i == 9 else rng.randint(0, 100))
        writer.writerow([f'case{seed}-v{i}', label, f'2026-10-01T18:{i:02}:00Z', value, 'fictional-case.csv'])
    return output.getvalue().encode('utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    parser.add_argument('--seed', type=int)
    args = parser.parse_args()
    # Exclusive creation avoids destroying an existing source or learner file.
    with args.output.open('xb') as stream:
        stream.write(PRACTICE if args.seed is None else independent(args.seed))
    print(f'Created fictional input: {args.output.name}')


if __name__ == '__main__':
    main()
