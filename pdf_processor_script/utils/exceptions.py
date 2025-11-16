"""
Defines domain-specific exceptions to provide clear, structured,
and recruiter-friendly error handling across the project.
"""

class PDFProcessorError(Exception):
    """Base exception for all PDFProcessor-related errors."""
    pass

class PDFProcessingError(PDFProcessorError):
    """Raised when a PDF operation (merge, split, rotate) fails."""
    def __init__(self, message: str):
        super().__init__(f"PDF Processing Error: {message}")

class ConfigLoadError(Exception):
    """Raised when application configuration fails to load or validate."""
    def __init__(self, message: str):
        super().__init__(f"Configuration Load Error: {message}")

class MissingFileError(Exception):
    """Raised when a required file is missing."""
    def __init__(self, filepath: str):
        super().__init__(f"Missing file: {filepath}")

class InvalidPDFError(Exception):
    """Raised when the PDF file is corrupted or invalid."""
    def __init__(self, filepath: str):
        super().__init__(f"Invalid PDF: {filepath}")
