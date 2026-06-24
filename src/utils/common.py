import yaml
from pathlib import Path
from box import ConfigBox
from src.logger import logger

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    with open(path_to_yaml) as f:
        content = yaml.safe_load(f)
        logger.info(f"yaml file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)

def create_directories(path_list: list, verbose=True):
    for path in path_list:
        Path(path).mkdir(parents=True, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")