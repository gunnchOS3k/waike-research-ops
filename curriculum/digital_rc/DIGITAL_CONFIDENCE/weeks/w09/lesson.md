# Week 9: Readable screens — measuring colour contrast

DCO-3909: the library's new event flyer uses pale grey text, and a patron with low vision cannot read it. Readability can be measured. The W3C's Web Content Accessibility Guidelines, WCAG 2.2, define a contrast ratio between text and background colours. Each colour's red, green, and blue values are converted to a relative luminance, a weighted brightness in which green counts most and blue least, and the ratio is the lighter luminance plus 0.05 divided by the darker luminance plus 0.05. Black on white is 21 to 1; identical colours are 1 to 1. Normal-size text needs at least 4.5 to 1 for level AA, and large text needs 3 to 1. The grey #767676 on white measures about 4.54 and just passes. One step lighter, #777777, measures about 4.48 and fails for normal text, even though most eyes cannot tell the two apart, which is exactly why you measure rather than guess. Use a contrast checker before printing or posting, and remember contrast is one accessibility check among many, not the whole job.

## Worked example

#767676 on #ffffff → 4.54:1 passes AA normal text; #777777 on #ffffff → 4.48:1 fails AA normal, passes AA large
