"""
Centralized rotating logging configuration for the PDF processing tool.

This module exposes a `get_logger` function used across the application
to ensure consistent logging behavior, properly formatted log entries,
and industry-grade management via RotatingFileHandler.
"""

import logging
from logging.handlers import RotatingFileHandler
import os


def get_logger(log_file: str) -> logging.Logger:
    """
    Create and configure a rotating logger instance.

    Args:
        log_file (str): Path to the log file from configuration.

    Returns:
        logging.Logger: A fully configured logger object.
    """

    # Ensures log directory exists before writing logs
    log_dir = os.path.dirname(log_file)
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger("pdf_processor")

    # Avoid duplicate handlers when called multiple times
    if not logger.hasHandlers():  
        # Rotating handler prevents oversized logs in long-term usage
        handler = RotatingFileHandler(
            log_file,
            maxBytes=2 * 1024 * 1024,  # 2MB log rotation threshold
            backupCount=5              # Keep last 5 rotated logs
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger
