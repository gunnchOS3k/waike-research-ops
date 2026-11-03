# Week 1: Fiber latency budget — light is slower in glass

Change request NIF-5101 asks whether a new 1,145 km fiber route between two regional exchanges can promise game servers a one-way delay under six milliseconds. Light in a vacuum covers about 299,792 km each second, but glass slows it by the fiber's group index, about 1.468, so the signal moves at roughly 204,000 km/s. Divide the route length by that speed: 1,145 km takes about 5.6067 milliseconds. That is propagation, and no upgrade fixes it short of a straighter path. Serialization is the time to clock a packet's bits onto the wire: 1,500 bytes is 12,000 bits, which takes 0.012 ms at one gigabit per second and would take ten times longer on a 100-megabit link. Add them for a one-way floor of about 5.619 ms, before any queueing or equipment delay. Route length is not the straight-line distance on a map; cables follow railways and roads, so ask for the measured route. Using the vacuum speed understates delay by about a third and leads to promises the backbone cannot keep.

## Worked example

1,145 km × 1.468 / 299,792.458 km/s = 5.6067 ms propagation; 1,500 B × 8 / 1 Gbit/s = 0.012 ms; one-way 5.6187 ms
