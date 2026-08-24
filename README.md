# Python Selenium Automation Boilerplate

This repository provides a starting point for Python Selenium projects using the Page Object Model (POM), pytest and helpers for assertions, utilities, reporting and an automatic PPTX generator that documents the architecture and step-by-step process.

Key features
- Page Object Model under `pages/`
- Tests under `tests/` using pytest and fixtures
- Utilities under `utils/`
- Assertion helpers under `asserts/`
- `scripts/generate_pptx.py` to build a PowerPoint deck documenting the project
- Supports Chrome and Firefox via webdriver-manager

Quick start
1. Create and activate a virtual environment

   python -m venv venv
   source venv/bin/activate  # mac/linux
   venv\Scripts\activate     # windows

2. Install dependencies

   pip install -r requirements.txt

3. Generate the documentation PPTX

   python scripts/generate_pptx.py --output docs/automation_presentation.pptx

4. Run tests and produce an HTML report

   pytest -v --html=reports/python_html_report.html --self-contained-html

Files & folders (high-level)
- pages/: Page objects (BasePage + pages)
- tests/: pytest tests and fixtures
- utils/: browser factory, config reader, logger, screenshot helper
- asserts/: centralized assertion helpers
- scripts/: helpers including PPTX generator
- config.ini: externalized configuration
- pytest.ini: pytest configuration

See the `docs/` folder for the generated PPTX (run the script to produce it locally).
