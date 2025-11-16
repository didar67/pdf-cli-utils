"""
Core package for the PDF Processor Script.

This package provides the essential components for PDF manipulation, configuration management,
and logging within the application. It encapsulates the core business logic and utilities
to ensure modularity, testability, and maintainability.

Modules included:
- pdf_handler: Handles PDF operations such as merging, splitting, and rotating.
- config_loader: Manages loading and validation of application configuration from YAML files.
- logger: Provides centralized logging configuration with rotating file handlers.

Usage:
    from core import PDFProcessor, load_config, get_logger
"""

from .pdf_handler import PDFProcessor
from .config_loader import load_config
from .logger import get_logger

__all__ = ["PDFProcessor", "load_config", "get_logger"]
