"""Configuration."""

from pathlib import Path


class Config:
    """Configuration."""

    test_data_dir: Path = Path("test_data").absolute()
    temp_dir: Path = test_data_dir / "temp"
