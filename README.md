# cicd-example-bad

A Python project intentionally containing bugs and errors, used to demonstrate
failure scenarios in the B-Team CI/CD system.

This repository contains:
- A project with a **logical bug** causing test failures
- A file with a **syntax error** causing a runtime failure

---

## Prerequisites

Make sure you have the B-Team CI/CD system installed and running before proceeding.
Refer to the main repository's README for installation instructions.

---

## Demo Commands

### 1. Run the failing-tests pipeline (tests will fail)
```bash
cicd run --name failing-tests
```

Expected output:

[Pipeline: failing-tests] Starting run #1
[Stage: test] Running job: run-tests ... ✗ failed
[Pipeline: failing-tests] Run #1 completed: FAILED
Job 'run-tests' failed with exit code 1:
FAILED tests/test_converter.py::test_celsius_to_fahrenheit - AssertionError


---

### 2. Run the syntax-error pipeline (runtime crash)
```bash
cicd run --name syntax-error
```

Expected output:

[Pipeline: syntax-error] Starting run #1
[Stage: build] Running job: check-syntax ... ✗ failed
[Pipeline: syntax-error] Run #1 completed: FAILED
Job 'check-syntax' failed with exit code 1:
File "src/broken_syntax.py", line 1
def greet(name)
^
SyntaxError: expected ':'

---

### 3. View report for a failed run

After running one or both pipelines:
```bash
cicd report --pipeline failing-tests
```
```bash
cicd report --pipeline failing-tests --run 1
```
```bash
cicd report --pipeline failing-tests --run 1 --stage test
```
```bash
cicd report --pipeline failing-tests --run 1 --stage test --job run-tests
```

---

## Additional Explanation

- `failing-tests.yaml`: The `celsius_to_fahrenheit` function in `converter.py` contains a bug in the formula (it is missing `+ 32`), which causes two test assertions to fail, resulting in the pipeline status being `failed`.

- `syntax-error.yaml`: The first line of `broken_syntax.py` is missing a colon, so Python crashes during the parsing stage, and the pipeline status becomes `failed`.

- Both of these failures are **runtime failures** (the pipeline YAML itself is valid), which is different from the validation failures produced by `cicd verify`.