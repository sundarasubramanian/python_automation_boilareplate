#!/usr/bin/env bash
# Convenience script to run pytest in parallel using pytest-xdist.
# Usage: ./scripts/run_parallel.sh <workers>

WORKERS=${1:-4}
REPORT=reports/python_html_report.html

mkdir -p reports
pytest -n ${WORKERS} -v --html=${REPORT} --self-contained-html

echo "Report saved to ${REPORT}"
