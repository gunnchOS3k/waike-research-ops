# WAIKE Guyana UPNOW — Signal and Sound Isolation Strategy

> **Conceptual only — not for construction**
> Expert review required before construction or field deployment.
> Requires licensed architect/engineer review before construction.


## Network emphasis

flood-resilient connectivity, elevated equipment, regional low-bandwidth routes

## Connectivity stack

- Wired Ethernet/fiber backbone (design assumption)
- Wi-Fi AP per learning zone (design assumption)
- Local edge cache (synthetic simulation)
- Offline content server where needed (design assumption)
- Student vs staff vs lab network segmentation (brief-derived)
- Emergency/backup connectivity mode (design assumption)

## Acoustic/RF tradeoff matrix

| Zone pair | Acoustic strategy | RF strategy |
|-----------|-------------------|-------------|
| classroom ↔ classroom | double-stud, sound-isolated | separate APs; wired backbone |
| classroom ↔ quiet room | high isolation | minimal RF in quiet room |
| lab ↔ corridor | moderate isolation | AP inside lab only |

> Research simulation only — not operational carrier or emergency service.
