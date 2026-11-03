# Week 3: NTN propagation delay — nadir one-way and round trip

SGA-1303 is the first physics week. A non-terrestrial network puts the base station, or a relay for it, on a satellite, and the first consequence is time. Light covers 299,792.458 km per second, so a low-Earth-orbit satellite directly overhead at 600 km is about 2.0014 ms away one way and 4.0028 ms round trip. A geostationary satellite at 35,786 km is about 119.37 ms one way, which is why GEO links feel sluggish for interactive traffic even with ample bandwidth. These are nadir numbers: the satellite straight above the user. At low elevation the slant range can be several times the altitude, so the real delay is longer, and the lab asks you to state geometry = nadir so nobody mistakes a lower bound for a link budget. The 3GPP NTN study, TR 38.811, discusses why terrestrial timing assumptions such as HARQ round trips and timing advance must be stretched for these distances. The grader recomputes your delay from the altitude you submit, so copying the LEO answer onto a GEO altitude fails, which is exactly the mistake this week is designed to catch.

## Worked example

h=600 km: one_way = 600 / 299792.458 km/s = 2.0014 ms; rtt = 4.0028 ms. GEO h=35786 km: one_way ≈ 119.37 ms
