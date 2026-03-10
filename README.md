# cicd-example-failing

A Python project intentionally containing bugs and validation errors, used to demonstrate
failure scenarios in the B-Team CI/CD system.

This repository contains:
- A project with a **logical bug** causing test failures at runtime
- An invalid pipeline definition (`example_bad_invalid.yaml`) demonstrating four validation errors

---

## Prerequisites

Make sure you have the B-Team CI/CD system installed and running before proceeding.
Refer to the main repository's README for installation instructions.

---

## Demo Commands

### 1. Validate a pipeline that fails validation

```bash
cicd verify .pipelines/example_bad_invalid.yaml
```

Expected output:
```
✗ Found 4 error(s) in '.pipelines/example_bad_invalid.yaml':
.pipelines/example_bad_invalid.yaml:5:1: Empty stage 'deploy' has no jobs assigned
.pipelines/example_bad_invalid.yaml:19:3: Job 'unit-tests' has an empty needs list. If defined, needs must contain at least one job name.
.pipelines/example_bad_invalid.yaml:26:3: Job 'check-format' needs 'lint' which is not defined
.pipelines/example_bad_invalid.yaml:33:3: Circular dependency detected: package -> release -> package
```

---

### 2. Run a pipeline that fails (test failure)

```bash
cicd run --name example_bad_default
```

Expected output:
```
Submitting pipeline 'example_bad_default' for execution...
✓ Pipeline queued successfully (run ID: 1)
Waiting for pipeline to complete...

✗ Pipeline failed.
Total time: 22s
Run ID: 1

The following jobs failed:
  ✗ test / unit-tests (exit code: 1)

For more details run: cicd report --pipeline example_bad_default --run 1
```

---

### 3. View report for a failed run

All runs for the pipeline:
```bash
cicd report --pipeline example_bad_default
```

Expected output:
```yaml
pipeline:
  name: example_bad_default
  runs:
  - run-no: 1
    status: failed
    git-repo: https://github.com/EstherrrC/cicd-example-bad.git
    git-branch: main
    git-hash: ac7ccd3ee0c61fbb2d05c2bb1281aee6f987d6db
    start: '2026-03-10T22:23:15.015462+00:00'
    end: '2026-03-10T22:23:20.817241+00:00'
```

Details for a specific run:
```bash
cicd report --pipeline example_bad_default --run 1
```

Details for a specific stage:
```bash
cicd report --pipeline example_bad_default --run 1 --stage test
```

Details for a specific job:
```bash
cicd report --pipeline example_bad_default --run 1 --stage test --job unit-tests
```

---

## Additional Notes

- The `add()` function in `src/main.py` contains a bug (`a - b` instead of `a + b`), causing `test_add` to fail — this is intentional to demonstrate a pipeline runtime failure.
- `example_bad_invalid.yaml` demonstrates all four validation rules: empty stage, empty needs list, undefined needs reference, and circular dependency. This file is intentionally invalid and **cannot be run**, only verified.
- Runtime failures (wrong test results) are different from validation failures (invalid YAML structure) — this repo demonstrates both.