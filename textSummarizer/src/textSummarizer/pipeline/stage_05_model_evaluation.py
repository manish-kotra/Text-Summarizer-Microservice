from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_eval import ModelEvaluation
from textSummarizer.logging import logger

class ModelEvalPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config = ConfigurationManager()
            data_config = config.get_model_eval_config()
            model_evaluator = ModelEvaluation(config=data_config)
            model_evaluator.evaluate()
            logger.info("Model evaluation completed successfully.")

        except Exception as e:
            logger.exception("Error occurred during model evaluation")
            raise e