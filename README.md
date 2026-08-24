# Generate both palettes for the PPTX

You can generate a colorful, modern PowerPoint for the automation docs using the provided script. By default it generates two variants (blue_teal and purple_orange).

Examples:

# Generate both variants (default)
python scripts/generate_pptx.py --palette both

# Generate only blue_teal variant
python scripts/generate_pptx.py --palette blue_teal --output docs/automation_presentation_blue_teal.pptx

# Generate only purple_orange variant
python scripts/generate_pptx.py --palette purple_orange --output docs/automation_presentation_purple_orange.pptx

Note: The script creates the PPTX files locally under docs/. We do NOT commit generated binaries by default. If you later want me to add one of the generated PPTX files into the repository, tell me which file and I will commit it.
