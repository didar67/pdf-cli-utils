"""
Unit tests for ConfigLoader.

Includes:
- YAML loading
- Pydantic validation
- Error handling
"""

import pytest
from core.config_loader import ConfigLoader, Settings
from pydantic import ValidationError
from pathlib import Path
import yaml

@pytest.fixture
def valid_config(tmp_path):
    """Create a valid temporary YAML config file."""
    config_data = {
        "app": {"name": "TestApp", "environment": "test", "version": "1.0"},
        "paths": {"output_dir": "out/", "log_dir": "logs/"},
        "logging": {"level": "INFO", "rotation_size_mb": 5, "backup_count": 3}
    }
    config_file = tmp_path / "settings.yaml"
    with open(config_file, "w") as f:
        yaml.safe_dump(config_data, f)
    return config_file

def test_load_valid_config(valid_config):
    """Test that ConfigLoader successfully loads a valid YAML config."""
    loader = ConfigLoader(str(valid_config))
    settings = loader.load()
    assert isinstance(settings, Settings)
    assert settings.app.name == "TestApp"

def test_invalid_config_raises(tmp_path):
    """Test that invalid config data raises validation error."""
    invalid_file = tmp_path / "invalid.yaml"
    with open(invalid_file, "w") as f:
        f.write("invalid_yaml: [missing fields")
    loader = ConfigLoader(str(invalid_file))
    with pytest.raises(Exception):
        loader.load()
