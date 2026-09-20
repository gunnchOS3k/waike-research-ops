# Week 9: ACLs that actually order, and the telnet we refuse

An ACL is a story told top to bottom. Deny tcp/23, permit tcp/443, deny *. Telnet is a classroom fossil we refuse at the edge. HTTPS to the library cache is allowed. Port 9 discard is denied by the star rule — implicit deny made visible.

DHCP snooping and ARP inspection are named so you can recognize a CCNA Security Fundamentals neighbor. We implement neither on silicon. We do write why a rogue DHCP under the table hands out 192.168.1.1 as a gateway and steals a cohort afternoon.

WPA3 is a wireless security word you should be able to place next to 'guest SSID is isolated.' This is not a wireless engineering course (that is WIRELESS_6G, still alive as an advanced track).

SSH not telnet, HTTPS not HTTP for staff tools, and no 'permit ip any any' at the top because that line is how ACLs become wallpaper.

## Worked example

decide(23)=deny, decide(443)=permit, decide(9)=deny. NAT still maps the inside host.
