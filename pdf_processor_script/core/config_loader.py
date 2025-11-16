"""
Handles loading and validating YAML configuration for the application.
Provides a clean, typed, and predictable config structure using Pydantic.
"""

import yaml
from pathlib import Path
from pydantic import BaseModel, Field, ValidationError


class LoggingConfig(BaseModel):
    level: str = Field(..., description="Log level for the application.")
    rotation_size_mb: int = Field(..., description="Log rotation size in MB.")
    backup_count: int = Field(..., description="Number of rotated log files to keep.")


class PathsConfig(BaseModel):
    output_dir: str = Field(..., description="Directory where output files are stored.")
    log_dir: str = Field(..., description="Directory where logs are stored.")


class AppConfig(BaseModel):
    name: str
    environment: str
    version: str


class Settings(BaseModel):
    app: AppConfig
    paths: PathsConfig
    logging: LoggingConfig


class ConfigLoader:
    """Loads and validates YAML-based configuration."""

    def __init__(self, config_path: str):
        self.config_path = Path(config_path)

    def load(self) -> Settings:
        # Ensure configuration file exists
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_path}")

        # Load YAML safely
        with open(self.config_path, "r") as file:
            raw_data = yaml.safe_load(file)

        # Validate and map to Settings model
        try:
            return Settings(**raw_data)
        except ValidationError as e:
            # Strict validation feedback for debugging config issues
            raise ValueError(f"Invalid configuration: {e}")


def load_config(config_path: str = "config/settings.yaml") -> Settings:
    """
    Helper function used by the application entrypoint.
    Simplifies loading validated application configuration.
    """

    loader = ConfigLoader(config_path)
    return loader.load()
