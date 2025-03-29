import os
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from textSummarizer.logging import logger
from pathlib import Path

@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox type.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        ConfigBox: Content of the YAML file.
    """
    try:
        with open(file_path) as file:
            content = yaml.safe_load(file)
            logger.info(f"YAML file {file_path} loaded successfully.")
            return ConfigBox(content)
        
    except BoxValueError as e:
        raise ValueError(f"Error parsing YAML file {file_path}: {e}")
    
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(dirs: list, verbose=True):
    """
    Creates directories if they do not exist.

    Args:
        dirs (list): List of directory paths to create.
    """
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        if verbose:
            logger.info(f"Directory {dir_path} created or already exists.")


@ensure_annotations
def get_size(file_path: str) -> str:
    """
    Returns the size of a file in a KB.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Size of the file in a KB.
    """
    try:
        size = round(os.path.getsize(file_path) / 1024, 2)
        return f"{size} KB"
    
    except Exception as e:
        raise e