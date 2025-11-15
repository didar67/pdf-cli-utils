"""
PDFProcessor class
-------------------
Handles all PDF operations (merge, split, rotate) in a clean,
testable, and scalable architecture for future PDF features.
"""

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from utils.exceptions import PDFProcessingError
from core.logger import get_logger

logger = get_logger(__name__)


class PDFProcessor:
    """Central processor for handling all PDF operations."""

    def __init__(self, input_files=None):
        """
        Initialize processor with optional input files list.
        
        Args:
            input_files (list[Path] | None): List of PDF paths.
        """
        self.input_files = (
            [Path(f) for f in input_files] if input_files else []
        )

    def merge_pdfs(self, output_path: str):
        """
        Merge multiple PDFs into a single output file.
        
        Args:
            output_path (str): Path for merged PDF.
        """
        if not self.input_files:
            raise PDFProcessingError("No PDF files provided for merging.")

        writer = PdfWriter()

        # Add pages from each file
        for pdf in self.input_files:
            try:
                reader = PdfReader(pdf)
                for page in reader.pages:
                    writer.add_page(page)
                logger.info(f"Merged: {pdf}")
            except Exception as e:
                logger.error(f"Failed merging {pdf}: {e}")
                raise PDFProcessingError(f"Error merging {pdf}") from e

        # Save output file
        try:
            with open(output_path, "wb") as f:
                writer.write(f)
            logger.info(f"Merged PDF saved at: {output_path}")
        except Exception as e:
            raise PDFProcessingError("Error writing merged PDF.") from e

    def split_pdf(self, input_pdf: str, output_dir: str):
        """
        Split a single PDF into multiple single-page PDFs.
        
        Args:
            input_pdf (str): Path to PDF to split.
            output_dir (str): Directory where split files will be stored.
        """
        input_pdf = Path(input_pdf)
        output_dir = Path(output_dir)

        try:
            reader = PdfReader(input_pdf)
        except Exception as e:
            raise PDFProcessingError("Cannot read input PDF.") from e

        # Create output files page-by-page
        for i, page in enumerate(reader.pages, start=1):
            writer = PdfWriter()
            writer.add_page(page)

            output_file = output_dir / f"{input_pdf.stem}_page_{i}.pdf"

            try:
                with open(output_file, "wb") as f:
                    writer.write(f)
                logger.info(f"Created split page: {output_file}")
            except Exception as e:
                raise PDFProcessingError(
                    f"Error writing page {i} during split."
                ) from e

    def rotate_pdf(self, input_pdf: str, output_pdf: str, angle: int):
        """
        Rotate all pages in a PDF by a given angle.
        
        Args:
            input_pdf (str): PDF to rotate.
            output_pdf (str): Rotated PDF output path.
            angle (int): Rotation angle (90, 180, 270).
        """
        try:
            reader = PdfReader(input_pdf)
        except Exception as e:
            raise PDFProcessingError("Cannot read input PDF.") from e

        writer = PdfWriter()

        # Apply rotation
        for page in reader.pages:
            page.rotate(angle)
            writer.add_page(page)

        # Save output
        try:
            with open(output_pdf, "wb") as f:
                writer.write(f)
            logger.info(f"Rotated PDF saved at: {output_pdf}")
        except Exception as e:
            raise PDFProcessingError("Error saving rotated PDF.") from e
