"""Public contract tests for the worked example, not protected assessment keys."""
import hashlib
import math
import unittest

from case_data import PRACTICE, independent
from ledger import analyze


class LedgerContract(unittest.TestCase):
    def test_source_bytes_and_ingest_counts(self):
        report = analyze(PRACTICE)
        self.assertEqual(report['source_sha256'], hashlib.sha256(PRACTICE).hexdigest())
        self.assertEqual((report['rows_in'], report['rows_out']), (6, 4))
        changed = PRACTICE.replace(b'20,fictional', b'21,fictional')
        self.assertNotEqual(analyze(changed)['source_sha256'], report['source_sha256'])

    def test_sql_executes_strict_predicate(self):
        self.assertEqual(analyze(PRACTICE)['selected_rows'], [['v3', 60], ['v4', 80]])
        self.assertEqual(analyze(PRACTICE, threshold=60)['selected_rows'], [['v4', 80]])
        self.assertEqual(analyze(PRACTICE, threshold=100)['selected_rows'], [])

    def test_missing_negative_and_zero_are_distinct(self):
        report = analyze(PRACTICE)
        self.assertEqual(report['rejected'], [{'visit_id': 'v5', 'reason': 'missing_headcount'}, {'visit_id': 'v6', 'reason': 'negative_headcount'}])
        self.assertAlmostEqual(report['missing_rate_raw'], 1 / 6)
        zero = PRACTICE.replace(b'20,fictional', b'0,fictional')
        self.assertEqual(analyze(zero)['rows_out'], 4)
        self.assertEqual(analyze(zero)['mean_headcount'], 45)

    def test_kpi_and_normalization(self):
        report = analyze(PRACTICE)
        self.assertEqual(report['mean_headcount'], 50)
        self.assertEqual(report['p95_nearest_rank'], 80)
        self.assertEqual(report['group_summary'], [{'pier_bay': 'bay_a', 'n': 3, 'mean_headcount': 40}, {'pier_bay': 'bay_b', 'n': 1, 'mean_headcount': 80}])

    def test_weighted_mean_is_not_mean_of_group_means(self):
        groups = analyze(PRACTICE)['group_summary']
        self.assertEqual(sum(g['n'] * g['mean_headcount'] for g in groups) / 4, 50)
        self.assertEqual(sum(g['mean_headcount'] for g in groups) / 2, 60)

    def test_join_loss_is_visible(self):
        report = analyze(PRACTICE, metadata=[('bay_a', 'North pier')])
        self.assertEqual(report['join'], {'inner_rows': 3, 'orphan_ids': ['v4']})

    def test_duplicate_join_keys_rejected(self):
        with self.assertRaisesRegex(ValueError, 'duplicate metadata'):
            analyze(PRACTICE, metadata=[('bay_a', 'North'), ('bay_a', 'Other')])

    def test_freshness_is_explicit_and_boundary_inclusive(self):
        self.assertEqual(analyze(PRACTICE)['freshness']['age_minutes'], 25)
        self.assertTrue(analyze(PRACTICE, sla_minutes=25)['freshness']['within_policy'])
        self.assertFalse(analyze(PRACTICE, sla_minutes=24)['freshness']['within_policy'])
        report = analyze(PRACTICE, now='2026-10-01T20:40:00+02:00')
        self.assertEqual(report['freshness']['age_minutes'], 25)

    def test_bad_clock_rejected(self):
        for now in ('2026-10-01T18:40:00', '2026-10-01T17:00:00Z', 'nonsense'):
            with self.subTest(now=now), self.assertRaises(ValueError):
                analyze(PRACTICE, now=now)

    def test_schema_duplicate_and_unknown_alias_rejected(self):
        for raw in (
            b'', b'PASS', PRACTICE.replace(b'headcount,', b'guessed_count,'),
            PRACTICE.replace(b'v2,bay_a', b'v1,bay_a'),
            PRACTICE.replace(b'Bay-A', b'Unknown'),
            PRACTICE.replace(b'20,fictional', b'2.5,fictional'),
            PRACTICE.replace(b'20,fictional', b'NaN,fictional'),
            PRACTICE.replace(b'20,fictional', b'20,extra,fictional'),
            PRACTICE.replace(b'20,fictional.csv', b'20'),
            b'x' * 65537,
        ):
            with self.subTest(raw=raw[:50]), self.assertRaises(ValueError):
                analyze(raw)

    def test_no_valid_observations_is_not_zero_kpi(self):
        raw = b'visit_id,pier_bay,ts_utc,headcount,source_file\nv1,bay_a,2026-10-01T18:00:00Z,,fixture.csv\n'
        with self.assertRaisesRegex(ValueError, 'no valid headcounts'):
            analyze(raw)

    def test_invalid_parameters_rejected(self):
        for value in (True, False, None, -1, '40', math.nan, math.inf):
            with self.subTest(value=value), self.assertRaises(ValueError):
                analyze(PRACTICE, threshold=value)
            with self.subTest(value=value), self.assertRaises(ValueError):
                analyze(PRACTICE, sla_minutes=value)

    def test_new_cases_are_reproducible_and_different(self):
        self.assertEqual(independent(731), independent(731))
        self.assertNotEqual(independent(731), independent(732))
        self.assertNotEqual(analyze(independent(731))['source_sha256'], analyze(independent(732))['source_sha256'])
        for seed in (0, 1, 731, 999999):
            report = analyze(independent(seed))
            self.assertEqual((report['rows_in'], report['rows_out']), (12, 10))
            self.assertFalse(report['competency_demonstrated'])
            self.assertEqual(report['instructor_review'], 'pending')

    def test_generator_rejects_invalid_seed(self):
        for seed in (True, '4', -1, 1000000):
            with self.subTest(seed=seed), self.assertRaises(ValueError):
                independent(seed)


if __name__ == '__main__':
    unittest.main()
