from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
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