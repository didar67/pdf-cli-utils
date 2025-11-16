"""
Entry point of the PDF Processor CLI tool.

This minimal orchestrator handles:
- Loading validated configuration
- Initializing centralized logger
- Delegating execution to the CLI parser
"""

from core.logger import get_logger
from core.config_loader import load_config
from cli.parser import run_cli
from utils.exceptions import ConfigLoadError

def main() -> None:
    """Bootstrap the PDF Processor application with minimal orchestration."""
    try:
        # Load validated YAML configuration
        config = load_config()

        # Initialize centralized application logger
        logger = get_logger(config.paths.log_dir + "/application.log")
        logger.info("Application initialized successfully.")

        # Pass logger and config to CLI dispatcher
        run_cli(config, logger)

    except ConfigLoadError as e:
        print(f"Configuration loading failed: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
