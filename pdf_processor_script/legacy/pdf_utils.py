"""
pdf_utils.py

Custom utility functions for PDF file operations including:
1. Merging multiple PDF files into one
2. Splitting a single PDF into individual pages
3. Rotating all pages of a PDF by a given angle
"""

import os
import logging
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(pdf_list, output_path):
    """Merge multiple PDF files and save into a single PDF"""
    merger = PdfWriter()

    for pdf_file in pdf_list:
        try:
            with open(pdf_file, "rb") as f:
                reader = PdfReader(f)
                merger.append(reader)
                logging.info(f"Merged file: {pdf_file}")

        except FileNotFoundError:
            logging.error(f"File not found: {pdf_file}")
        except PermissionError:
            logging.error(f"Access denied: {pdf_file}")
        except Exception as err:
            logging.error(f"Unexpected error while merging {pdf_file}: {str(err)}")

    try:
        with open(output_path, "wb") as out:
            merger.write(out)
        logging.info(f"Merged PDF saved at: {output_path}")

    except Exception as err:
        logging.error(f"Failed to save merged PDF: {str(err)}")


def split_pdf(pdf_path, output_dir):
    """Split a single PDF file into separate pages and save each as an individual PDF."""
    try:
        with open(pdf_path, "rb") as f:
            reader = PdfReader(f)

            for i, page in enumerate(reader.pages):
                writer = PdfWriter()
                writer.add_page(page)
                output_file = os.path.join(output_dir, f"page_{i+1}.pdf")
                with open(output_file, "wb") as out:
                    writer.write(out)
                logging.info(f"Saved split page: {output_file}")

    except FileNotFoundError:
        logging.error(f"File not found: {pdf_path}")
    except PermissionError:
        logging.error(f"Access denied: {pdf_path}")
    except Exception as err:
        logging.error(f"Error during splitting {pdf_path}: {str(err)}")


def rotate_pdf(pdf_path, output_path, degree):
    """Rotate every page of a PDF file by a specific degree and save the result."""
    try:
        with open(pdf_path, "rb") as f:
            reader = PdfReader(f)
            writer = PdfWriter()

            for i, page in enumerate(reader.pages):
                page.rotate(degree)
                writer.add_page(page)
                logging.info(f"Rotated page {i+1} by {degree} degrees")

            with open(output_path, "wb") as out:
                writer.write(out)
            logging.info(f"Rotated PDF saved to: {output_path}")

    except FileNotFoundError:
        logging.error(f"Source PDF not found: {pdf_path}")
    except PermissionError:
        logging.error(f"Access denied for file: {pdf_path}")
    except Exception as err:
        logging.error(f"Rotation failed for {pdf_path}: {str(err)}")

