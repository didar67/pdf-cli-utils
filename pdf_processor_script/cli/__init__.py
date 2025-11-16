"""
CLI Module for PDF Processor Script.

This module provides the command-line interface for the PDF Processor application,
enabling users to perform operations such as merging, splitting, and rotating PDF files
through structured subcommands. It maintains modularity by separating CLI parsing and
execution logic, supporting features like dry-run modes and future extensions.

Exposed functions:
- build_parser: Constructs the argument parser for CLI commands.
- run_cli: Executes the parsed CLI commands using the PDFProcessor.
"""

from .parser import build_parser, run_cli

__all__ = ["build_parser", "run_cli"]
