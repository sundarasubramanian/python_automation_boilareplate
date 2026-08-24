# Secrets & Credentials: Jenkins and GitHub Actions guidance

This document describes recommended approaches for storing and using secrets (credentials, API tokens, passwords) in CI systems and local development.

General rules
- Never commit secrets into the repository (no passwords, tokens, or private keys).
- Prefer built-in secret stores provided by CI systems (Jenkins Credentials, GitHub Secrets).
- Limit scope & rotate secrets regularly.

1) Jenkins

Jenkins Credentials types (examples):
- Username with password
- Secret text
- Secret file
- SSH username with private key

Using credentials in a Pipeline (Declarative) - example

credentials:
  - id: 'MY_CRED_ID'

Example usage in a Declarative Jenkinsfile pipeline:

pipeline {
  agent any
  environment {
    // Inject credential as env var
    MY_SECRET = credentials('my-secret-text-id')
  }
  stages {
    stage('Run tests') {
      steps {
        sh 'python -m venv venv'
        sh '. venv/bin/activate && pip install -r requirements.txt'
        sh '. venv/bin/activate && BROWSER=chrome HEADLESS=true pytest -v --html=reports/python_html_report.html'
      }
    }
  }
}

Notes:
- Use the `withCredentials` block for more complex needs and to avoid exposing secrets in console logs.
- Store credentials in Jenkins credentials store (Manage Jenkins > Credentials) and refer to them by ID.

2) GitHub Actions

- Store secrets in the repository or organization Secrets (Settings > Secrets and Variables > Actions).
- Access secrets via `${{ secrets.MY_SECRET }}` in the workflow and map to environment variables for steps.

Example snippet in a workflow step:

steps:
  - name: Checkout
    uses: actions/checkout@v4
  - name: Install dependencies
    run: |
      python -m venv venv
      . venv/bin/activate
      pip install -r requirements.txt
  - name: Run tests
    env:
      BROWSER: chrome
      HEADLESS: true
      API_TOKEN: ${{ secrets.API_TOKEN }}
    run: |
      . venv/bin/activate
      pytest -v --html=reports/python_html_report.html --self-contained-html

3) Local development: .env and config_local.ini

- For local development it is convenient to store non-committed local overrides in a `.env` file or `config_local.ini`.
- Add `.env` and `config_local.ini` to `.gitignore` so they are never committed.

Example `.env` (DO NOT COMMIT):

BROWSER=chrome
HEADLESS=false
API_TOKEN=super-secret-token

How to read .env in Python (recommended)
- Use the python-dotenv package to load .env into environment variables.

Example code:

from dotenv import load_dotenv
import os

load_dotenv()  # reads .env into environment variables
browser = os.environ.get('BROWSER', 'chrome')

4) Best practices
- Limit privileges of secrets (use tokens with narrow scopes).
- Rotate secrets and revoke unused keys.
- Audit secret access and avoid printing them in logs.
- For browser automation credentials, consider storing test user accounts in a secure store and inject via CI at runtime.

