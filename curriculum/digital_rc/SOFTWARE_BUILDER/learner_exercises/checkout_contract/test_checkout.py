"""Worked-example tests. Independent assignment requires additional cases."""
import unittest
from checkout import Checkout

class ContractTests(unittest.TestCase):
    def setUp(self): self.app=Checkout()
    def tearDown(self): self.app.close()
    def test_get_does_not_change_availability(self):
        self.assertEqual(self.app.request('GET','demo-1')['outcome'], 'available')
        self.assertEqual(self.app.request('GET','demo-1')['outcome'], 'available')
    def test_desk_can_checkout_once(self):
        self.assertEqual(self.app.request('POST','demo-1','desk')['status'],201)
        self.assertEqual(self.app.request('POST','demo-1','desk')['status'],409)
    def test_reader_cannot_mutate(self):
        self.assertEqual(self.app.request('POST','demo-1','reader')['status'],403)
        self.assertEqual(self.app.request('GET','demo-1')['outcome'],'available')
    def test_unknown_item(self):
        self.assertEqual(self.app.request('GET','missing')['status'],404)
    def test_parameter_binding_treats_input_as_data(self):
        self.assertEqual(self.app.request('GET',"demo-1' OR 1=1 --")['status'],404)
        self.assertEqual(self.app.request('GET','demo-1')['status'],200)
    def test_log_is_bounded_to_status_and_outcome(self):
        self.app.request('GET','demo-1')
        self.assertEqual(set(self.app.events[0]), {'status','outcome'})

if __name__=='__main__': unittest.main()
