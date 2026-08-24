# Sample Test Matrix and Parallel Run Examples

This document provides examples of a test matrix you can use to run the suite across different browsers and configurations.

1) Simple matrix (local)
- Browser: chrome
- Browser: firefox
- Mode: headless / headed
- Workers: 1, 4

Example runs:
- Run Chrome headless: BROWSER=chrome HEADLESS=true pytest -v
- Run Firefox headed: BROWSER=firefox HEADLESS=false pytest -v

2) Parallel execution (pytest-xdist)
- Run 4 parallel workers on the default browser from config:
  ./scripts/run_parallel.sh 4

- Use environment matrix in CI (example conceptual):
  - job-1: BROWSER=chrome, WORKERS=4
  - job-2: BROWSER=firefox, WORKERS=4

3) Cross-browser matrix (example matrix table)
| Job | Browser | Headless | Workers |
|-----|---------|----------|---------|
| 1   | chrome  | true     | 4       |
| 2   | firefox | true     | 4       |
| 3   | chrome  | false    | 2       |

Notes:
- Ensure the agent has Chrome and/or Firefox browser binaries installed for webdriver-manager to download drivers that match.
- In lightweight CI you can run each browser in a separate job to avoid contention.
