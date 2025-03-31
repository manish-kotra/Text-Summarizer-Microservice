import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataTrasformationConfig
from transformers import  AutoTokenizer
from datasets import load_from_disk


class DataTransformation:
    def __init__(self, config: DataTrasformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)


    def convert_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    
    def transform(self):
        logger.info("Transforming the dataset...")
        dataset = load_from_disk(self.config.data_path)
        dataset = dataset.map(self.convert_to_features, batched=True)
        dataset.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))
        logger.info("Dataset transformation completed.")