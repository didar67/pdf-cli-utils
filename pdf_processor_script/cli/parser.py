"""
Provides structured subcommands (merge, split, rotate) for the PDF Processor.
Keeps main.py minimal and supports future extensions like dry-run or verbose mode.
"""

import argparse
from core.pdf_handler import PDFProcessor
from utils.exceptions import PDFProcessingError


def build_parser() -> argparse.ArgumentParser:
    """Builds and returns the configured CLI parser."""
    parser = argparse.ArgumentParser(
        description="PDF Processor CLI - merge, split, rotate PDFs"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="Available operations"
    )

    # MERGE 
    merge = subparsers.add_parser(
        "merge", help="Merge multiple PDF files into one"
    )
    merge.add_argument(
        "-i", "--input", required=True, nargs="+",
        help="Input PDF file paths"
    )
    merge.add_argument(
        "-o", "--output", required=True,
        help="Output merged PDF path"
    )
    merge.add_argument(
        "--dry-run", action="store_true",
        help="Preview merge without creating output"
    )

    # SPLIT 
    split = subparsers.add_parser(
        "split", help="Split a PDF into single-page PDFs"
    )
    split.add_argument(
        "-i", "--input", required=True,
        help="Input PDF file path"
    )
    split.add_argument(
        "-o", "--output-dir", required=True,
        help="Directory for split PDFs"
    )
    split.add_argument(
        "--dry-run", action="store_true",
        help="Preview split without writing files"
    )

    # ROTATE
    rotate = subparsers.add_parser(
        "rotate", help="Rotate a PDF by a given angle"
    )
    rotate.add_argument(
        "-i", "--input", required=True,
        help="Input PDF file path"
    )
    rotate.add_argument(
        "-o", "--output", required=True,
        help="Rotated PDF output path"
    )
    rotate.add_argument(
        "-a", "--angle", required=True, type=int,
        choices=[90, 180, 270],
        help="Rotation angle"
    )
    rotate.add_argument(
        "--dry-run", action="store_true",
        help="Preview rotation without writing output"
    )

    return parser


def run_cli(config, logger):
    """
    Dispatch CLI commands to PDFProcessor operations.
    Keeps main.py minimal and modular.
    """
    parser = build_parser()
    args = parser.parse_args()

    pdf_processor = PDFProcessor(input_files=getattr(args, "input", None))

    try:
        if args.command == "merge":
            if not args.dry_run:
                pdf_processor.merge_pdfs(args.output)
            logger.info("Merge command executed successfully.")

        elif args.command == "split":
            if not args.dry_run:
                pdf_processor.split_pdf(args.input, args.output_dir)
            logger.info("Split command executed successfully.")

        elif args.command == "rotate":
            if not args.dry_run:
                pdf_processor.rotate_pdf(args.input, args.output, args.angle)
            logger.info("Rotate command executed successfully.")

        else:
            parser.print_help()

    except PDFProcessingError as e:
        logger.error(f"Operation failed: {e}")
        raise
