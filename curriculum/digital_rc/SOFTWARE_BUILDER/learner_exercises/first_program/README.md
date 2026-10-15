# Your first program: turn a capacity question into a tested function

Start here before the Checkout contract example if variables, functions or automated tests are unfamiliar. You need the Digital Confidence file-saving and capacity activities, a plain-text editor, and Python 3.11 or later installed on a computer you control. No administrator privileges, packages, web account or network are required. If the runtime is unavailable, use your authorized teaching environment; do not install a random executable to bypass that prerequisite.

By the end you should be able to explain the difference between text and numbers, call a function with different inputs, predict a branch, diagnose a failed test and revise your own code. Passing these example tests is practice; it is not independent evidence of those skills.

## 1. Save and run a program

Download `capacity.py` and `test_capacity.py` together into a new folder you own. Show filename extensions in your file manager if necessary; `capacity.py.txt` is a text document with the wrong name for these commands. Open a terminal in that folder. A terminal accepts commands as text; its current folder determines where relative filenames are found. Run:

```
python3 --version
python3 capacity.py
```

Where the Windows Python launcher is already installed, use `py -3` in place of `python3`. The first command identifies the interpreter, which reads and runs Python code. The second names a file to run; typing the filename into an editor does not execute it. Expected output is:

```
Usable free: 25.000%; meets fixture policy
```

The program uses fictional storage values. It does not inspect or modify your real disk. Do not paste your home-directory name or other personal information into evidence.

## 2. Read one statement at a time

A variable gives a value a name. In `total = 256`, `=` assigns a value; it is different from `==`, which compares values. The integer `256` supports arithmetic. The text `"256"` is a string; it must be validated and converted before arithmetic. This example deliberately accepts only whole-number GiB inputs, so it rejects strings, fractional measurements and booleans rather than silently guessing what they mean.

`def capacity(total, used, reserve):` defines a reusable function. Indented lines are its body. Parameters are local names receiving the caller's inputs. `capacity(256, 180, 12)` calls that function with three arguments. Parentheses group the subtraction before division: `(256 - 180 - 12) / 256 * 100` is 25.0. All three values must use the same unit. The reserve is separate from used capacity in this fixture; subtracting a reserve already included in used would be a different model.

`if free_percent >= 15:` selects a branch. The threshold is a teaching policy, not a universal operating-system requirement. A below-policy result can be an accurate answer. `return` sends a result back to the caller. The returned dictionary has named entries, accessed as `result['free_percent']`; it is not a database and is not saved after the process exits.

Before changing any code, predict `capacity(256, 220, 12)`. The remaining 24 GiB is 9.375%, so the policy branch should say `below`. Change only the example call at the bottom, save, rerun and compare. Restore the original call afterward. If the output stays unchanged, confirm that you saved the same file that the terminal runs.

## 3. Reject impossible inputs before computing

A total of zero cannot be a divisor. Negative capacity and used-plus-reserve exceeding total are invalid for this fixture. The function raises `ValueError` for these cases. An exception stops the normal return path and describes why the input was rejected. We do not catch every exception and print a success message: rejection is part of the contract.

Try a deliberate error in the example call: `capacity(0, 0, 0)`. Read the final exception line, then locate the filename and line number above it. Expected result: `ValueError: total must be positive`. Restore the valid call. Keep the error and repaired output in your fictional practice journal. A traceback is diagnostic evidence; it does not mean the computer has been damaged.

## 4. Read and run an automated test

Run:

```
python3 -m unittest -v test_capacity.py
```

`-m unittest` asks Python to run its standard test tool. It imports the named test file. Importing `capacity.py` defines its function, but the `if __name__ == '__main__':` guard keeps the demonstration print from running during import. Expected result: nine tests pass, including invalid inputs. Each assertion compares observed behavior with an independently specified expectation. A green run only covers these cases.

In `test_exact_threshold`, a 200 GiB volume with 160 used and 10 reserved leaves 30 GiB, exactly 15%. The test expects `meets`. Temporarily change the function's comparison from `>=` to `>` and run the suite. That boundary test must fail. Read expected versus actual, restore `>=`, and run again. Do not change the test to hide the failure.

Troubleshooting: `ModuleNotFoundError` usually means one file is missing, renamed or in another folder. `SyntaxError` often means an unmatched quote, bracket or colon. `IndentationError` means the block indentation is inconsistent; compare the reference's spaces. A failed assertion means the code ran but differed from the expected behavior. Check the named case before editing unrelated lines. Work in a copy if you need to preserve the original.

## 5. Independent variation and review

Create a separate `capacity_plan.py`. Write a function taking total, used, separate reserve and a proposed **additional** workload in whole GiB. It must report free percentage after the workload, whether the workload physically fits, and whether the resulting state meets the same 15% policy. Define what happens when it does not fit; do not return an ordinary successful capacity result for an impossible state. Keep physically fitting and policy-compliant as separate concepts.

Choose your own fictional inputs. Include a fitting case above policy, a fitting case below policy, an exactly-at-policy case, a workload that exceeds free capacity, zero total, a negative workload, and a text input. Calculate expected results before running your code. Write tests for each and demonstrate one deliberate defect that a test catches. No reference solution for this independent variation is included here.

Deliver your source, tests, expected-results table, before/failure/repair output and a short explanation of one limitation. Explain the branches in your own words. A reviewer checks arithmetic, validation, the distinct fit/policy decisions, meaningful tests and your revision process. They may ask for changed inputs or a live explanation. Revision is expected when a criterion is unmet; submission alone does not award mastery. If you used AI or other help, identify what it supplied and what you independently checked.

Return to Software Builder Week 1 to connect a plain-language requirement to this function's contract. Continue to the Checkout contract worked example once you can explain the parameter, return value, branch and boundary test without reading a script. Git, HTTP and SQLite will introduce additional concepts; this local program does not implement those systems.

AI assistance contributed to this guide, code and tests. Human technical and educational acceptance is pending. Repository software licensing applies; no third-party assets or real learner data are included.
