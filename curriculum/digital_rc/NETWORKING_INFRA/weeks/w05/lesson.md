# Week 5: DNS TTL — planning a change the world sees late

NIF-5505 is a cutover: a public website moves to new servers at t = 5,000 seconds and the old servers will be switched off soon after. Resolvers that looked up the name keep the answer for its time to live, and RFC 1034 lets them reuse it without asking again. A resolver that cached the record at t = 3,000 with a TTL of 3,600 seconds will hand out the old address until t = 6,600, so its users see the old site for 1,600 seconds after the change. In the worst case a resolver caches the old answer one second before the change and stays stale for the whole TTL, 3,600 seconds. The fix is planning: lower the TTL to something short, such as 300 seconds, at least one old TTL before the change, so by t = 1,400 at the latest, and raise it again once the new servers are stable. Keep the old servers answering until the worst-case window has passed. A change is not live when the zone file is saved; it is live when the last cache has expired.

## Worked example

TTL 3600; resolver cached at t=3000 → expires 6600; record changed at 5000 → stale window 1600 s; worst case 3600 s; lower TTL by t=1400
