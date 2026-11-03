# Week 6: Email authentication — passing is not the same as aligned

SOC-2606 compares two invoices that both claim to come from Harbor Pay. SPF checks whether the sending server is allowed to send for the envelope's return-path domain. DKIM checks a signature made with a key published by the domain in the signature's d= tag. Both can pass for a domain that has nothing to do with the address the reader sees in the From line. DMARC closes that gap with alignment: at least one passing check must belong to the same organisational domain as the visible From address. Under relaxed alignment, subdomains count, so in message A the From address mail.harborpay.example, the return path bounce.harborpay.example, and the DKIM domain harborpay.example all share harborpay.example, and DMARC passes. Message B also shows SPF pass and DKIM pass, but both checks vouch for bulk-sender.example while the From line says harborpay.example, so DMARC fails. That is exactly the shape of a convincing spoof, and a user who sees 'SPF pass' in a header viewer will be fooled unless someone on the desk explains alignment.

## Worked example

A: From mail.harborpay.example, SPF via bounce.harborpay.example, DKIM d=harborpay.example → aligned → DMARC pass; B: From harborpay.example, SPF/DKIM pass for bulk-sender.example → not aligned → DMARC fail
