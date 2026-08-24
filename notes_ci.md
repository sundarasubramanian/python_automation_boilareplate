# Jenkins CI notes for this repo

Steps to add a Jenkins job for running the automation suite:

1. Create a new Jenkins Pipeline or Freestyle job.
2. In the job configuration, add a Git SCM with the repository URL: https://github.com/sundarasubramanian/python_automation_boilareplate.git
3. Add build steps:
   - Setup Python (install or use a virtualenv)
   - pip install -r requirements.txt
   - python scripts/generate_pptx.py --output automation_presentation.pptx  # optional
   - pytest -v --html=reports/python_html_report.html --self-contained-html
4. Post-build actions:
   - Archive the `reports/` directory and generated `automation_presentation.pptx` artifact
   - Publish HTML reports using the "HTML Publisher" plugin (point to reports/python_html_report.html)
5. Configure credentials for any environment variables or secrets via Jenkins Credentials
6. (Optional) Run tests inside a container or use nodes labeled with browsers and required drivers

Notes on Jenkins agents and browsers:
- For Chrome & Firefox, either install browsers on the agent or use Docker images that include them.
- GeckoDriver/ChromeDriver will be downloaded automatically via webdriver-manager at runtime.
