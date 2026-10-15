# Packet model: calculate, predict, compare

Requirements: Python 3.11+, including the standard `ipaddress` library. Save both `.py` files in the same empty practice folder. Run `python3 -m unittest -v test_network_model.py` there (or `py -3 -m unittest -v test_network_model.py` with the Windows Python launcher). Expected result: seven tests pass. An import error means you should check the filenames and starting directory before changing code.

This model sends no packets, opens no sockets and changes no network settings. It models data-segment arithmetic without options/retransmissions, IPv4 prefix arithmetic, longest-prefix selection and TTL decrement. It does not parse bytes, implement TCP, exchange routing protocols, transmit ICMP or validate a physical network.

Predict the output before running. Add a more-specific /32 route and a test showing that it takes priority over /26. Change TTL to 1 and explain why a matching route does not permit forwarding. Add your own /31 and /32 arithmetic tests and state their point-to-point/host-route conventions. The existing canonical CIDR lab has its own acceptance contract; do not assume this example's /32 convention automatically satisfies it.

Independent work: add a test for equal-length duplicate route entries and document the model's tie behavior. Does that establish a real router's policy? Explain why not. Deliberately replace longest-prefix selection with shortest-prefix selection, observe the failed test, then restore and rerun. Preserve the failing output as evidence of a test that detects a defect.

No real learner or network measurements are present. AI assistance contributed to code, tests and instruction. Human technical and educational acceptance remains pending.
