# Week 2: Storage units — why a 500 GB drive shows 465 GiB

DCO-3202 is a NO_AI week; work the division on paper. A patron bought a '500 GB' drive and thinks the store cheated her because the computer shows about 465 GB. Nobody cheated. Drive makers count in powers of ten, so a gigabyte is 1,000,000,000 bytes. Many operating systems count in powers of two, where a gibibyte, GiB, is 1,073,741,824 bytes, and then label the result GB anyway. Divide 500,000,000,000 by 1,073,741,824 and you get about 465.66, the same drive described in a bigger unit. The same confusion bites when deciding whether something will fit. Her phone holds 1,200 photos at about 4.2 MB each, where MB means a million bytes, so the folder is 5.04 billion bytes. In the binary unit that is about 4.69 GiB, and the laptop says 4.5 GiB free. It will not fit, even though '5 GB into 4.5' felt close. Write the unit beside every number, convert both sides to the same unit before comparing, and leave room to spare, because a completely full disk makes most computers slow and unstable.

## Worked example

500 GB = 500×10^9 B = 465.66 GiB; 1,200 photos × 4.2 MB = 5.04×10^9 B = 4.694 GiB > 4.5 GiB free → does not fit
