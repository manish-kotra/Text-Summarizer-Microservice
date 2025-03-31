from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    required_files: list


@dataclass(frozen=True)
class DataTrasformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path