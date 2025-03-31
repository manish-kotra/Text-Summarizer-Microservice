import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files(self) -> bool:
        try :
            validation_status = None
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            for file in all_files:
                if file not in self.config.required_files:
                    validation_status = False
                    with open(self.config.status_file, "w") as f:
                        f.write(f"File {file} is not present in the directory \n")
                        f.write(f"Validation status: {validation_status} \n")
                        logger.info(f"File {file} is not present in the directory")
                else:
                    validation_status = True
                    with open(self.config.status_file, "w") as f:
                        f.write(f"All required files are present in the directory \n")
                        f.write(f"Validation status: {validation_status} \n")
                        logger.info(f"All required files are present in the directory")

            return validation_status
        
        except Exception as e:
            raise e