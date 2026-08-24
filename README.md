# Python Selenium Automation Boilerplate

[![Build Status](https://img.shields.io/badge/build-manual%20CI-lightgrey)](https://github.com/sundarasubramanian/python_automation_boilareplate)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

This repository provides a starting point for Python Selenium projects using the Page Object Model (POM), pytest and helpers for assertions, utilities, reporting and an automatic PPTX generator that documents the architecture and step-by-step process.

Summary of additions in this commit
- pytest-rerunfailures added to requirements and enabled by default via pytest.ini (2 automatic reruns)
- A sample flaky test (tests/test_flaky_example.py) demonstrates retry behaviour
- README enhancements: badges, clearer commands, CI notes and environment variable guidance
- docs/secrets.md: guidance for storing credentials in Jenkins and GitHub Actions and example .env handling

Quick start
1. Clone the repo
   git clone https://github.com/sundarasubramanian/python_automation_boilareplate.git
   cd python_automation_boilareplate

2. Create & activate a virtual environment
   python -m venv venv
   source venv/bin/activate  # mac/linux
   venv\Scripts\activate     # windows

3. Install dependencies
   pip install -r requirements.txt

4. Generate the PPTX documentation (creates docs/automation_presentation.pptx)
   python scripts/generate_pptx.py --output docs/automation_presentation.pptx
   (or) python main.py --pptx --output docs/automation_presentation.pptx

5. Run tests and generate HTML report
   pytest -v --html=reports/python_html_report.html --self-contained-html

Notes about retries / flaky tests
- This project includes pytest-rerunfailures to rerun failed tests automatically. By default pytest.ini sets `--reruns=2` so failed tests will be retried up to 2 times before being marked as failed.
- You can override reruns at the command line: `pytest -v --reruns=0` to disable reruns.

Environment variables
- BROWSER: chrome or firefox (overrides config.ini)
- HEADLESS: true / false (overrides config.ini headless)
- WORKERS: used by scripts/run_parallel.sh to set pytest-xdist workers

CI notes (short)
- For Jenkins: create a Pipeline that checks out the repo, sets up Python, installs requirements, sets BROWSER and HEADLESS as needed, runs pytest and archives `reports/`.
- For GitHub Actions: create a matrix job (chrome/firefox) that sets the BROWSER env and runs the same pytest commands; upload the HTML report as an artifact.

Further docs
- docs/test_matrix.md — cross-browser and parallel examples
- docs/secrets.md — guidance on credentials and secret storage

