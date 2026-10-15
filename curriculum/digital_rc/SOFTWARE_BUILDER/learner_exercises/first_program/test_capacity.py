import unittest
from capacity import capacity

class CapacityContract(unittest.TestCase):
    def test_example(self):
        self.assertEqual(capacity(256, 180, 12), {'free_percent': 25.0, 'policy': 'meets'})
    def test_below_policy_is_valid(self):
        self.assertEqual(capacity(256, 220, 12), {'free_percent': 9.375, 'policy': 'below'})
    def test_exact_threshold(self):
        self.assertEqual(capacity(200, 160, 10), {'free_percent': 15.0, 'policy': 'meets'})
    def test_full_volume(self):
        self.assertEqual(capacity(100, 90, 10), {'free_percent': 0.0, 'policy': 'below'})
    def test_empty_volume(self):
        self.assertEqual(capacity(100, 0, 0), {'free_percent': 100.0, 'policy': 'meets'})
    def test_zero_total(self):
        with self.assertRaisesRegex(ValueError, 'positive'):capacity(0, 0, 0)
    def test_impossible_capacity(self):
        for values in [(100, -1, 0), (100, 1, -1), (100, 95, 10), (-100, 0, 0)]:
            with self.subTest(values=values),self.assertRaises(ValueError):capacity(*values)
    def test_text_and_fractional_inputs(self):
        for value in ['100', 100.0, None, []]:
            with self.subTest(value=value),self.assertRaises(TypeError):capacity(value, 0, 0)
    def test_boolean_is_not_measurement(self):
        with self.assertRaises(TypeError):capacity(100, True, 0)

if __name__ == '__main__':unittest.main()
