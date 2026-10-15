import unittest
from triage import authorized,triage,timeline
class TriageTests(unittest.TestCase):
    def test_allow_read(self):self.assertTrue(authorized('analyst','read_redacted'))
    def test_deny_action(self):self.assertFalse(authorized('analyst','propose_containment'))
    def test_unknown_role_denied(self):self.assertFalse(authorized('unknown','read_redacted'))
    def test_threshold_is_not_verdict(self):
        result=triage([{'actor_alias':'actor-a','outcome':'failed'}]*3)
        self.assertEqual(result,[{'actor_alias':'actor-a','failed_count':3,'disposition':'investigate'}])
    def test_below_threshold(self):self.assertEqual(triage([{'actor_alias':'actor-a','outcome':'failed'}]*2),[])
    def test_timezone_normalization(self):
        events=[{'id':'later','time':'2026-01-01T12:00:00Z'},{'id':'earlier','time':'2026-01-01T12:30:00+01:00'}]
        self.assertEqual(timeline(events)[0]['id'],'earlier')
    def test_missing_timezone_rejected(self):
        with self.assertRaises(ValueError):timeline([{'time':'2026-01-01T12:00:00'}])
if __name__=='__main__':unittest.main()
