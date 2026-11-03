# Week 5: Spreadsheet formulas — let the sheet do the arithmetic

DCO-3505 is a monthly budget written on the back of an envelope that never adds up the same way twice. Move it into a spreadsheet: labels in column A, amounts in column B, one row per item. Rent is 650, food 240, the bus pass 55, the phone 35, and savings 120. Instead of typing the total, write =SUM(B2:B6) and the sheet answers 1,100, then keeps answering correctly when the phone bill changes. =AVERAGE(B2:B6) gives 220, the typical line, and =MAX(B2:B6) finds the largest amount, which belongs to rent. To see how much of the month food takes, divide its cell by the total cell, =B3/B7, and format the result as a percentage: about 21.82 percent. The habit worth keeping is that numbers you typed live in one place and every other number is a formula pointing at them. A total typed by hand goes stale the first time anything changes, and that is how budgets quietly stop matching reality. Save the file somewhere you will find it, with a name that says what and when.

## Worked example

rent 650, food 240, bus pass 55, phone 35, savings 120 → =SUM 1100, =AVERAGE 220, =MAX rent, food share =240/1100 = 21.82%
