import unittest
from packet_fixture import PositiveDnsCache, checksum, crafted_frame, ipv6_prefix, lease_status, parse_frame, report


class PacketFixtureContract(unittest.TestCase):
    def test_actual_header_fields(self):
        frame=crafted_frame()
        parsed=parse_frame(frame)
        self.assertEqual(len(frame),54)
        self.assertEqual(parsed['dst_mac'],'aa:aa:aa:aa:aa:01')
        self.assertEqual((parsed['ip_header_bytes'],parsed['ip_total_bytes'],parsed['ttl'],parsed['proto']),(20,40,4,6))
        self.assertEqual((parsed['src_ip'],parsed['dst_ip']),('192.0.2.14','198.51.100.9'))
        self.assertEqual((parsed['src_port'],parsed['dst_port']),(50000,443))
        self.assertEqual(checksum(frame[14:34]),0)

    def test_parsed_ttl_changes_forwarding_not_constants(self):
        self.assertEqual(report()['decision'],{'action':'forward','port':'eth1','ttl':3,'prefix':'198.51.100.0/24'})
        self.assertEqual(report(1)['decision'],{'action':'drop','reason':'ttl_expired'})
        self.assertNotEqual(report()['parsed']['source_sha256'],report(1)['parsed']['source_sha256'])
        self.assertFalse(report()['physical_measurement'])
        self.assertFalse(report()['competency_demonstrated'])

    def test_changed_destination_uses_default(self):
        self.assertEqual(report(8,'203.0.113.4')['decision']['port'],'uplink')

    def test_truncation_wrong_type_and_corruption_rejected(self):
        frame=crafted_frame()
        for bad in (b'',frame[:13],frame[:33],frame[:-1],frame.hex(),frame[:12]+b'\x86\xdd'+frame[14:],frame[:22]+b'\x07'+frame[23:]):
            with self.subTest(bad=bad),self.assertRaises(ValueError):parse_frame(bad)

    def test_invalid_ip_header_shapes(self):
        frame=bytearray(crafted_frame())
        for first in (0x65,0x44,0x4f):
            changed=bytearray(frame);changed[14]=first
            with self.assertRaises(ValueError):parse_frame(bytes(changed))
        changed=bytearray(frame);changed[16:18]=(19).to_bytes(2,'big')
        with self.assertRaises(ValueError):parse_frame(bytes(changed))

    def test_fragment_and_tcp_header_limits(self):
        frame=bytearray(crafted_frame())
        # Change IPv4 fragment flag, then repair header checksum so the fragment rule is tested.
        frame[20:22]=(0x2000).to_bytes(2,'big');frame[24:26]=b'\0\0'
        frame[24:26]=checksum(bytes(frame[14:34])).to_bytes(2,'big')
        with self.assertRaisesRegex(ValueError,'fragment'):parse_frame(bytes(frame))
        frame=bytearray(crafted_frame());frame[46]=0xf0
        with self.assertRaisesRegex(ValueError,'TCP'):parse_frame(bytes(frame))

    def test_cache_hit_and_exact_expiry(self):
        cache=PositiveDnsCache();authority={'desk.example':('203.0.113.14',300)}
        self.assertEqual(cache.lookup('desk.example',0,authority)['how'],'fixture_authority')
        authority['desk.example']=('203.0.113.15',300)
        self.assertEqual(cache.lookup('DESK.example',299,authority),{'address':'203.0.113.14','how':'cache','remaining_seconds':1})
        self.assertEqual(cache.lookup('desk.example',300,authority)['address'],'203.0.113.15')

    def test_zero_ttl_and_missing_name_are_honest(self):
        cache=PositiveDnsCache();authority={'desk.example':('203.0.113.14',0)}
        self.assertEqual(cache.lookup('desk.example',0,authority)['how'],'fixture_authority')
        self.assertEqual(cache.lookup('desk.example',0,authority)['how'],'fixture_authority')
        self.assertEqual(cache.lookup('other.example',1,authority)['how'],'not_in_fixture')

    def test_cache_bad_clock_and_authority_rejected(self):
        cache=PositiveDnsCache();cache.lookup('desk.example',10,{})
        for now in (True,-1,9,10.5):
            with self.assertRaises(ValueError):cache.lookup('desk.example',now,{})
        with self.assertRaises(ValueError):cache.lookup('private.internal',10,{})
        with self.assertRaises(ValueError):cache.lookup('desk.example',10,{'desk.example':('203.0.113.14',-1)})

    def test_lease_before_at_and_after_expiry(self):
        self.assertEqual(lease_status(100,3600,3699),{'state':'active','remaining_seconds':1})
        self.assertEqual(lease_status(100,3600,3700),{'state':'expired','remaining_seconds':0})
        self.assertEqual(lease_status(100,3600,4000)['state'],'expired')
        for args in ((True,3600,100),(100,0,100),(100,3600,99)):
            with self.assertRaises(ValueError):lease_status(*args)

    def test_ipv6_not_ipv4_host_subtraction(self):
        self.assertEqual(ipv6_prefix('2001:db8:20::7/64'),{'network':'2001:db8:20::/64','address_count':2**64,'has_broadcast':False})
        self.assertEqual(ipv6_prefix('2001:db8::7/128')['address_count'],1)
        with self.assertRaises(ValueError):ipv6_prefix('192.0.2.4/24')

    def test_bad_ttl_and_odd_checksum(self):
        self.assertEqual(checksum(b'\0'),65535)
        for ttl in (-1,256,True,'4'):
            with self.assertRaises(ValueError):crafted_frame(ttl)


if __name__=='__main__':unittest.main()
