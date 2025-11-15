"""
Entry point of the PDF Processor CLI tool.
Initializes logging and delegates execution to the CLI parser.
"""

from core.logger import get_logger
from cli.parser import run_cli
from core.config_loader import load_config


def main() -> None:
    """Application bootstrap function."""
    
    # Load configuration file (logging path included)
    config = load_config()

    # Initialize application-wide logger
    logger = get_logger(config.logging.log_file)
    logger.info("Application initialized successfully.")

    # Pass logger + config to CLI dispatcher
    run_cli(config, logger)


if __name__ == "__main__":
    main()
