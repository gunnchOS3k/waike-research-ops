# Week 8: Imaging a lab — unicast one by one versus one multicast stream

ISH-4808: forty refurbished laptops need the same 32 GB system image before the library's coding club opens. Image sizes are in bytes and network links in bits, so start by multiplying by eight: 256 gigabits per copy. On a gigabit link that really delivers about 70 percent of its rating, one copy takes about 366 seconds, a little over six minutes. Sending the image to each laptop separately, unicast, repeats that forty times through the same server port: about 244 minutes, more than four hours. Multicast sends one stream that every listening machine receives together, so in the ideal case the whole lab finishes in about the time of a single copy, roughly six minutes. Real networks need switches that handle multicast properly, and one slow or faulty laptop can hold the session back, so plan a fallback to unicast for stragglers. Whatever the method, check one finished machine against a list of expected settings before releasing the rest, and record which image version went onto which serial numbers.

## Worked example

32 GB image × 8 = 256 Gbit ÷ (1 Gbit/s × 0.7) = 365.7 s per stream; 40 machines unicast ≈ 243.8 min; multicast ≈ 6.1 min
