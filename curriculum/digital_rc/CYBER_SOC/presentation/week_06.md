# Night Shift 6: Email authentication — passing is not the same as aligned

On the board: A: From mail.harborpay.example, SPF via bounce.harborpay.example, DKIM d=harborpay.example → aligned → DMARC pass; B: From harborpay.example, SPF/DKIM pass for bulk-sender.example → not aligned → DMARC fail
