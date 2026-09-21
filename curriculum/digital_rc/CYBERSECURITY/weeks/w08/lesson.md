# Week 8: Authorized toy parser — detect the length lie, do not grow an exploit kit

Berkeley CS161 uses authorized vulnerable targets in a course VM. We take the depth pattern, not the projects. Harbor's course CTF is a length-prefixed toy parser: first byte claims payload length. The unsafe parser trusts it. A message `\x14short` claims 20 bytes and only has 5. The safe parser raises.

You will write a detector and a safe parser. You will not write shellcode, you will not scan random IPs, you will not reuse anyone's exam binary. This is the only vulnerability lab in the course and it is sandboxed on purpose.

Security+ threats/vulnerabilities domain is the alignment label. Mitigations here are bounds checks and refusing to run the unsafe function in production images.

If you find a real bug in WAIKE software outside this fixture, you report it — you do not 'practice' on it.

## Worked example

unsafe(\x14short) returns a short slice (the lie). safe(\x14short) raises ValueError. safe(\x04abcd)==b'abcd'.
