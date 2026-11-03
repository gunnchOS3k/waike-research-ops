# Week 5: ATT&CK mapping — describe behaviour, not villains

SOC-2505 gives the desk five behaviours seen this week and asks for a shared vocabulary. MITRE ATT&CK is a public catalogue of attacker techniques, each with an ID and one or more tactics that say what the attacker was trying to achieve. Many failed SSH logins from one address are T1110, Brute Force, under credential access. A never-before-seen account logging in at three in the morning with a correct password is T1078, Valid Accounts, which ATT&CK lists under several tactics because stolen credentials help an intruder get in, stay in, and blend in. A spoofed invoice attachment is T1566, Phishing, under initial access. PowerShell launched with an encoded command line is T1059, Command and Scripting Interpreter, under execution, and files renamed with a .locked suffix beside a ransom note are T1486, Data Encrypted for Impact. Mapping lets the day shift, the detection engineers, and management talk about the same thing. It does not tell you who did it. Plenty of groups use the same techniques, so the lab requires actor_attribution_claim to stay false.

## Worked example

B1 brute force → T1110 credential_access; B3 spoofed invoice → T1566 initial_access; B5 .locked files → T1486 impact; actor_attribution_claim false
