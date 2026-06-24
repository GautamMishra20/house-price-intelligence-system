import shutil
from pathlib import Path
from src.entity.config_entity import DataIngestionConfig
from src.logger import logger

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def ingest_data(self):
        if not Path(self.config.source_data_path).exists():
            raise FileNotFoundError(
                f"Source data not found at {self.config.source_data_path}"
            )

        shutil.copy(
            src=self.config.source_data_path,
            dst=self.config.ingested_data_path,
        )
        logger.info(
            f"Copied data from {self.config.source_data_path} "
            f"to {self.config.ingested_data_path}"
        )