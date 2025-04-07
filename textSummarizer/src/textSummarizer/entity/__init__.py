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


@dataclass(frozen=True)
class TrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    per_device_eval_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: int
    gradient_accumulation_steps: int


@dataclass(frozen=True)
class ModelEvalConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path