"""
Utility modules for the PDF Processor Script.

This package provides various utility functions, classes, and exceptions
used throughout the PDF processing application. It includes custom error
handling, helper functions, and other supporting code to facilitate
PDF merging, splitting, and related operations.

Modules:
    - exceptions: Custom exception classes for error handling.
"""

# Import key exceptions to make them easily accessible
from .exceptions import PDFProcessingError, MissingFileError, InvalidPDFError

__all__ = ['PDFProcessingError', 'MissingFileError', 'InvalidPDFError']
