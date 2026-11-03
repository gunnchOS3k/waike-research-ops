# Week 8: Availability — redundancy in parallel, single points in series

NIF-5808: a regional exchange's design has two core routers sharing traffic, each available 99.9 percent of the time, followed by one power feed at 99.95 percent and one fiber uplink at 99.99 percent. The question from management is how many minutes a year customers should expect to lose. A redundant pair fails only when both members are down at once, so its unavailability is the product of theirs: 0.001 times 0.001 is one in a million, making the pair 0.999999 available, assuming failures are independent. Parts in series all have to work, so their availabilities multiply: 0.999999 times 0.9995 times 0.9999 is about 0.9993991. A year has 525,600 minutes, so expected downtime is about 315.9 minutes, more than five hours, almost all of it from the single power feed. Spending more on routers would barely move the result; a second feed would. Shared causes such as one power strip feeding both routers break the independence assumption and must be designed away.

## Worked example

pair 1 − (0.001 × 0.001) = 0.999999; × 0.9995 × 0.9999 = 0.9993991; downtime (1 − A) × 525,600 = 315.9 min/yr
