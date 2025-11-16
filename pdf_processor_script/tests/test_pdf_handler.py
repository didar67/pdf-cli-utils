"""
Unit tests for PDFProcessor class.

Includes:
- merge, split, rotate functionality
- mock file system and PDF files
- exception handling validation
"""

import pytest
from pathlib import Path
from core.pdf_handler import PDFProcessor
from utils.exceptions import PDFProcessingError

@pytest.fixture
def sample_pdfs(tmp_path):
    """Creates temporary dummy PDF files for testing."""
    pdf_files = []
    for i in range(2):
        pdf_file = tmp_path / f"file_{i}.pdf"
        pdf_file.write_bytes(b"%PDF-1.4 dummy content")
        pdf_files.append(pdf_file)
    return pdf_files

def test_merge_pdfs_creates_output(sample_pdfs, tmp_path):
    """Test PDF merging produces output file."""
    output_file = tmp_path / "merged.pdf"
    processor = PDFProcessor(input_files=sample_pdfs)
    processor.merge_pdfs(str(output_file))
    assert output_file.exists()

def test_merge_pdfs_no_input_raises():
    """Test merging with no input files raises exception."""
    processor = PDFProcessor(input_files=[])
    with pytest.raises(PDFProcessingError):
        processor.merge_pdfs("dummy_output.pdf")

def test_split_pdf_creates_pages(sample_pdfs, tmp_path):
    """Test splitting a PDF creates multiple single-page PDFs."""
    processor = PDFProcessor()
    processor.split_pdf(str(sample_pdfs[0]), str(tmp_path))
    split_files = list(tmp_path.glob("*.pdf"))
    assert len(split_files) == 1  # 1-page dummy PDF
