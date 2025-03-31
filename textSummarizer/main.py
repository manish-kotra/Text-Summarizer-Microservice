from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"{'>'*20} {STAGE_NAME} started {'<'*20}")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f"{'>'*20} {STAGE_NAME} completed {'<'*20} \n\n")
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"{'>'*20} {STAGE_NAME} started {'<'*20}")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f"{'>'*20} {STAGE_NAME} completed {'<'*20} \n\n")

except Exception as e:
    logger.exception(e)
    raise e