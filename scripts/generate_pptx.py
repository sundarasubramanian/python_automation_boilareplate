"""Build a small PowerPoint presentation describing the automation architecture."""
from pptx import Presentation
from pptx.util import Inches


def add_slide(prs, title, content):
    layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(layout)
    slide.shapes.title.text = title
    body = slide.shapes.placeholders[1].text_frame
    for i, line in enumerate(content.split('\n')):
        if i == 0:
            body.text = line
        else:
            p = body.add_paragraph()
            p.text = line


def build_presentation(output_path='docs/automation_presentation.pptx'):
    prs = Presentation()
    # Title slide
    slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(slide_layout)
    slide.shapes.title.text = 'Python Selenium Automation Boilerplate'
    slide.placeholders[1].text = 'Architecture, files and how-to guide'

    add_slide(prs, 'Objectives', 'Provide a reusable baseline for web UI automation\nPage Object Model (POM)\npytest-based tests\nUtilities & assertions')
    add_slide(prs, 'Repository Structure', 'pages/: Page objects\ntests/: pytest tests\nutils/: helpers\nasserts/: assertion helpers\nscripts/: utilities (PPTX generator)')
    add_slide(prs, 'Files and purpose', '.gitignore: ignore artifacts\n.pylintrc: lint rules\nconfig.ini: env config\npytest.ini: pytest settings\nrequirements.txt: dependencies')
    add_slide(prs, 'Running tests', '1) pip install -r requirements.txt\n2) pytest -v --html=reports/python_html_report.html\n3) Check reports/ for screenshots and html report')
    add_slide(prs, 'Asserts / pages / tests / utils', 'pages/: POM classes to separate locators & actions\ntests/: test flows and assertions\nutils/: driver factory, config, logger, screenshots\nasserts/: centralized assertions')
    add_slide(prs, 'CI / Jenkins notes', 'Add a job to checkout the repo, set up Python, install requirements, run pytest, archive reports and screenshots. See README for detailed steps.')

    prs.save(output_path)


if __name__ == '__main__':
    build_presentation()
    print('Presentation generated')
