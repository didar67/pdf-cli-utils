"""
pdf_tool.py

A professional-grade CLI tool for merging, splitting, and rotating PDF files.
Built with argparse, configparser, and logging for automation and scripting needs.

"""
import os 
import argparse
import logging
import configparser
from pdf_utils import merge_pdfs, split_pdf, rotate_pdf

def setup_logger(log_file):
    """ 
    Configure the logging system to write logs to a file.
    Creates the log directory if it doesn't exist.
    """
    log_directory = os.path.dirname(log_file)
    os.makedirs(log_directory, exist_ok=True)

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def main():
    """
    Entry point of the PDF CLI tool.
    Handles user arguments, configuration loading, and command dispatch
    """
    # Loading configuration from config.ini
    config = configparser.ConfigParser()
    config.read("config.ini")

    output_directory = config['PDF']['output_dir']
    log_file = config['PDF']['log_file']

    # Initialize logger
    setup_logger(log_file)

    # Setup argument parser
    parser = argparse.ArgumentParser(description='Command-line tool to merge, split, and rotate PDF documents')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Subcommand: merge
    merge_cmd = subparsers.add_parser('merge', help='Merge multiple PDF files into a single PDF')
    merge_cmd.add_argument('files', nargs='+', help='Input PDF files to be merged')
    merge_cmd.add_argument('-o', '--output', default='merged.pdf', help='Name of the merged output file')

    # Subcommand: split
    split_cmd = subparsers.add_parser('split', help='Split a single PDF into multiple one-page PDFs') 
    split_cmd.add_argument('file', help='PDF file to be split page by page')

    # Subcommand: rotate
    rotate_cmd = subparsers.add_parser('rotate', help='Rotate pages in a PDF by a specified degree')
    rotate_cmd.add_argument('file', help='Target PDF file to rotate')
    rotate_cmd.add_argument('degree', choices=[90, 180,270], type=int, help='Degrees to rotate the PDF pages (90, 180, or 270)')
    rotate_cmd.add_argument('-o', '--output', default='rotated.pdf', help='Output filename after rotation')

    # Parse cli arguments
    args = parser.parse_args()

    # Ensure output directory exists
    os.makedirs(output_directory, exist_ok=True)

    # Handle commands

    if args.command == 'merge':
        output_path = os.path.join(output_directory, args.output)
        merge_pdfs(args.files,output_path)

    elif args.command == 'split':
        split_pdf(args.file, output_directory)

    elif args.command == 'rotate':
        output_path = os.path.join(output_directory, args.output)
        rotate_pdf(args.file, output_path, args.degree)


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        logging.error(f"Unexpected error occured: {err}")
        print("❌ An unexpected error occurred. Please check the log file for details.")
    finally:
        print("✅ PDF CLI tool execution finished.")
              