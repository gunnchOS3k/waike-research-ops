# Week 9: ACLs that actually order, and the telnet we refuse

An ACL is a story told top to bottom. Deny tcp/23, permit tcp/443, deny *. Telnet is a classroom fossil we refuse at the edge. HTTPS to the library cache is allowed. Port 9 discard is denied by the star rule — implicit deny made visible.

DHCP snooping and ARP inspection are named so you can recognize a CCNA Security Fundamentals neighbor. We implement neither on silicon. We do write why a rogue DHCP under the table hands out 192.168.1.1 as a gateway and steals a cohort afternoon.

WPA3 is a wireless security word you should be able to place next to 'guest SSID is isolated.' This is not a wireless engineering course (that is WIRELESS_6G, still alive as an advanced track).

SSH not telnet, HTTPS not HTTP for staff tools, and no 'permit ip any any' at the top because that line is how ACLs become wallpaper.

## Concept and scope

An ordered access-control list applies its configured match and decision policy. A broad early permit can make a later deny unreachable. NAT translation is not a substitute for an explicit authorization policy.

## Guided practice

Model first-match rules: deny destination port 23; permit port 443; deny everything else. Trace ports 23, 443 and 9. Expected results: deny, permit, deny. Swap the final deny to the first position and predict that all three requests are denied. Treat ports as fixture fields, not proof of the application running on them.

## Independent evidence

Add source-prefix conditions and test a case just outside the allowed prefix. Show the ordered rules and matching rule index. Do not apply this experimental policy to a live firewall. Include an approved rollback plan for any future operational exercise.

## Worked example

decide(23)=deny, decide(443)=permit, decide(9)=deny. NAT still maps the inside host.
