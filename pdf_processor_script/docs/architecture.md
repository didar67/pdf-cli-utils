# architecture.md

# PDF Processor Script — Architecture Overview

## Core Modules

### core/pdf_handler.py

* Central PDFProcessor class handles all operations: merge, split, rotate.
* Uses PyPDF2 for PDF manipulation.
* Integrated with centralized logger for operational traceability.

### core/logger.py

* Provides `get_logger` function for application-wide logging.
* Implements RotatingFileHandler to maintain log file sizes.
* Standardized log format ensures consistent observability.

### core/config_loader.py

* Loads and validates YAML-based configuration using Pydantic.
* Ensures typed access to paths, logging, and application settings.

## CLI Module (cli/parser.py)

* Argument parser separated from main.py.
* Subcommands: merge, split, rotate.
* Supports future enhancements like dry-run.
* Modular execution ensures testable CLI interface.

## Utils (utils/exceptions.py)

* Custom exceptions for PDF processing and configuration errors.
* Clear error flow improves debuggability and maintainability.

## Tests (tests/)

* Unit tests for PDFProcessor and ConfigLoader modules.
* Mocked filesystem and YAML validation tests ensure reliability.

## Entry Point (main.py)

* Minimal bootstrap: config load → logger init → CLI dispatch.
* Promotes modularity and recruiter-friendly readability.

## Config (config/settings.yaml)

* Contains application, logging, and path configurations.
* Centralized configuration management enables cloud readiness.

## Legacy Folder

* Stores old scripts for reference.
* Ensures historical traceability for recruiters.

## Future Scalability

* Async processing for large PDFs
* Web API integration
* Expanded PDF features (encrypt, watermark, metadata)

## License

* MIT License applied for professional open-source usage
