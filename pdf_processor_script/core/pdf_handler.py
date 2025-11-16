"""
Handles all PDF operations (merge, split, rotate) using a clean,
testable, and modular architecture suitable for production use.
"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from utils.exceptions import PDFProcessingError
from core.logger import get_logger

logger = get_logger(__name__)


class PDFProcessor:
    """Central processor for handling all PDF operations."""

    def __init__(self, input_files: list[str] | None = None):
        """
        Initialize processor with optional input files list.

        Args:
            input_files (list[str] | None): List of PDF file paths.
        """
        # Normalize inputs to Path objects
        self.input_files = [Path(f) for f in input_files] if input_files else []

    def merge_pdfs(self, output_path: str) -> None:
        """
        Merge multiple PDFs into a single output file.

        Args:
            output_path (str): Destination path for merged PDF.
        """
        if not self.input_files:
            raise PDFProcessingError("No PDF files provided for merging.")

        writer = PdfWriter()

        # Add pages from each input PDF
        for pdf in self.input_files:
            try:
                reader = PdfReader(pdf)
                for page in reader.pages:
                    writer.add_page(page)
                logger.info(f"Merged: {pdf}")
            except Exception as e:
                logger.error(f"Failed merging {pdf}: {e}")
                raise PDFProcessingError(f"Error merging {pdf}") from e

        # Save merged file
        try:
            with open(output_path, "wb") as file:
                writer.write(file)
            logger.info(f"Merged PDF saved at: {output_path}")
        except Exception as e:
            raise PDFProcessingError("Error writing merged PDF.") from e

    def split_pdf(self, input_pdf: str, output_dir: str) -> None:
        """
        Split a PDF into multiple single-page PDF files.

        Args:
            input_pdf (str): Path to the PDF file to split.
            output_dir (str): Output directory for generated page files.
        """
        input_path = Path(input_pdf)
        output_path = Path(output_dir)

        try:
            reader = PdfReader(input_path)
        except Exception as e:
            raise PDFProcessingError("Cannot read input PDF.") from e

        # Create each page as a separate PDF file
        for index, page in enumerate(reader.pages, start=1):
            writer = PdfWriter()
            writer.add_page(page)

            page_file = output_path / f"{input_path.stem}_page_{index}.pdf"

            try:
                with open(page_file, "wb") as file:
                    writer.write(file)
                logger.info(f"Created split page: {page_file}")
            except Exception as e:
                raise PDFProcessingError(
                    f"Error writing page {index} during split."
                ) from e

    def rotate_pdf(self, input_pdf: str, output_pdf: str, angle: int) -> None:
        """
        Rotate all pages in a PDF by a given angle.

        Args:
            input_pdf (str): Input PDF path.
            output_pdf (str): Output path for rotated PDF.
            angle (int): Rotation angle (90, 180, 270).
        """
        input_path = Path(input_pdf)

        try:
            reader = PdfReader(input_path)
        except Exception as e:
            raise PDFProcessingError("Cannot read input PDF.") from e

        writer = PdfWriter()

        # Apply rotation
        for page in reader.pages:
            page.rotate(angle)
            writer.add_page(page)

        # Save rotated file
        try:
            with open(output_pdf, "wb") as file:
                writer.write(file)
            logger.info(f"Rotated PDF saved at: {output_pdf}")
        except Exception as e:
            raise PDFProcessingError("Error saving rotated PDF.") from e
