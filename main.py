"""Main CLI for quick tasks: generate PPTX or run a smoke demo."""
import argparse
import subprocess
from scripts.generate_pptx import build_presentation


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pptx', action='store_true', help='Generate PPTX documentation')
    parser.add_argument('--output', default='docs/automation_presentation.pptx')
    args = parser.parse_args()

    if args.pptx:
        build_presentation(args.output)
        print(f'PPTX generated: {args.output}')
    else:
        print('No action specified. Use --pptx to generate the presentation.')


if __name__ == '__main__':
    main()
