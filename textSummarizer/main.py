from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_tranformation import DataTransformationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"{'>'*20} {STAGE_NAME} started {'<'*20}")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f"{'>'*20} {STAGE_NAME} completed {'<'*20} \n\n")
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"{'>'*20} {STAGE_NAME} started {'<'*20}")
    pipeline = DataValidationTrainingPipeline()
    pipeline.main()
    logger.info(f"{'>'*20} {STAGE_NAME} completed {'<'*20} \n\n")
    
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"{'>'*20} {STAGE_NAME} started {'<'*20}")
    pipeline = DataTransformationTrainingPipeline()
    pipeline.main()
    logger.info(f"{'>'*20} {STAGE_NAME} completed {'<'*20} \n\n")

except Exception as e:
    logger.exception(e)
    raise e