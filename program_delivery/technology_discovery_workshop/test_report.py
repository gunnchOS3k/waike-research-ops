import unittest
from assemble_report import summarize,CRITERIA
class ObservationReport(unittest.TestCase):
    def row(self,code,state='observed',attested='yes'):return {'participant_code':code,'reviewer_attested':attested,**{k:state for k in CRITERIA}}
    def test_mixed_review_preserves_pending_and_negative(self):
        rows=[self.row('P01'),self.row('P02','needs_revision'),self.row('P03','not_observed','no')];r=summarize(rows)
        self.assertEqual(r['participation_records_supplied'],3);self.assertEqual(r['instructor_reported_all_criteria_observed'],1)
        self.assertEqual(r['criteria']['restore'],{'needs_revision':1,'not_observed':1,'observed':1});self.assertFalse(r['course_completion_awarded'])
    def test_empty_does_not_invent_participants(self):self.assertEqual(summarize([])['participation_records_supplied'],0)
    def test_bad_codes_duplicates_unknown_states(self):
        for rows in [[self.row('Actual Name')],[self.row('P01'),self.row('P01')],[self.row('P01','pass')]]:
            with self.assertRaises(ValueError):summarize(rows)
    def test_unattested_observation_rejected(self):
        with self.assertRaises(ValueError):summarize([self.row('P01',attested='no')])
if __name__=='__main__':unittest.main()
