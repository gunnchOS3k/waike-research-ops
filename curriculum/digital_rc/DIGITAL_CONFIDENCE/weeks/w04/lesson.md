# Week 4: Reading a link — the real address is at the right end

DCO-3404 is a text message that says a bank account is locked and offers a link. Before tapping, read the address the way a computer does. Skip the https:// and stop at the first single slash after it; what sits between is the hostname. Read the hostname from the right end, label by label, because the rightmost labels say who owns it. In https://account.harborbank.example.verify-login.example.net/session the hostname is account.harborbank.example.verify-login.example.net, and its last two labels are example.net. The bank's name near the left is just decoration chosen by whoever owns example.net, which is not the bank. So the call is: do not open. Real organisations rarely ask you to log in from a message; type the bank's address yourself or use its app. Some country endings use three labels, such as .co.uk, so the rule 'last two labels' is a starting point, and the course's examples use the reserved .example endings so nobody is sent anywhere real. When unsure, show the message to the library desk rather than replying.

## Worked example

https://account.harborbank.example.verify-login.example.net/session → hostname ends in example.net → not harborbank.example → do not open
