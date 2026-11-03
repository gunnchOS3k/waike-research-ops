# Week 3: Passwords and passphrases — strength is length times choice

DCO-3303 starts with a sticky note that says P@ssw0rd! and a question: is this strong? Strength depends on how the password was chosen, not on how it looks. If every character is picked at random from a pool, the number of possibilities is the pool size raised to the length, and we measure it in bits: length times log2 of the pool. Four words drawn at random from a 7,776-word dice list give about 51.7 bits. Eight characters drawn at random from the 95 printable keyboard symbols give about 52.6 bits. Twelve random lowercase letters give about 56.4 bits, stronger than either, because length grows strength faster than adding symbols. P@ssw0rd! scores far lower than its nine characters suggest, because guessing tools try dictionary words with common swaps first. The NIST digital identity guidance, SP 800-63B, favours long memorable secrets, checking them against lists of known-breached passwords, and changing them when there is evidence of compromise rather than on a fixed calendar. Use a different secret on every site, and let a password manager remember them.

## Worked example

4 diceware words: 4×log2(7776) = 51.70 bits; 8 random printable: 8×log2(95) = 52.56; 12 random lowercase: 12×log2(26) = 56.41
