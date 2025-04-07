from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.logging import logger


class TrainingPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        try:
            config = ConfigurationManager()
            data_config = config.get_trainer_config()
            model_trainer = ModelTrainer(config=data_config)
            model_trainer.train()
        except Exception as e:
            raise e