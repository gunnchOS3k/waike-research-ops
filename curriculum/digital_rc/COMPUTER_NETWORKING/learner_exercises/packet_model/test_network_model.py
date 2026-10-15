import unittest
from network_model import segment_count, ipv4_summary, forward
class PacketModelTests(unittest.TestCase):
    def test_mtu_arithmetic(self): self.assertEqual(segment_count(2000),2)
    def test_empty_stream(self): self.assertEqual(segment_count(0),0)
    def test_invalid_header_budget(self):
        with self.assertRaises(ValueError): segment_count(20,40)
    def test_subnet(self): self.assertEqual(ipv4_summary('192.0.2.70/26'),{'network':'192.0.2.64','broadcast':'192.0.2.127','usable':62})
    def test_longest_prefix(self): self.assertEqual(forward('192.0.2.70',8,[('0.0.0.0/0','uplink'),('192.0.2.64/26','desk')])['port'],'desk')
    def test_expired_ttl(self): self.assertEqual(forward('192.0.2.70',1,[('0.0.0.0/0','uplink')])['reason'],'ttl_expired')
    def test_missing_route(self): self.assertEqual(forward('192.0.2.70',8,[])['reason'],'no_route')
if __name__=='__main__': unittest.main()
