# NETWORKING_INFRA — NOC mentor notes, week 5

**Board work:** TTL 3600; resolver cached at t=3000 → expires 6600; record changed at 5000 → stale window 1600 s; worst case 3600 s; lower TTL by t=1400

**Whiteboard:** ask one trainee to derive lab_nif_dns_ttl from its inputs before checking.

**Watch for:** Assuming a DNS change is live when the zone file is saved.
