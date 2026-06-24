from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_data_path: Path
    ingested_data_path: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    data_path: Path
    status_file: Path
    all_schema: dict