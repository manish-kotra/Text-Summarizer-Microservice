from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        config = ConfigurationManager()

    def main(self):
        try:
            config = ConfigurationManager()
            data_config = config.get_data_transformation_config()
            data_validation = DataTransformation(config=data_config)
            data_validation.transform()
        except Exception as e:
            raise e