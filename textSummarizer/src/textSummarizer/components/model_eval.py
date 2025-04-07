import torch
from transformers import (AutoModelForSeq2SeqLM, AutoTokenizer)
from tqdm import tqdm
from datasets import load_from_disk
from evaluate import load
import pandas as pd
from textSummarizer.entity import ModelEvalConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvalConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(config.model_path)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def generate_batch_sized_chunks(self, list_of_elements, batch_size):
        """Split the dataset into smaller batches that we can process simultaneously.
        Yield successive batch-sized chunks from list_of_elements."""
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i : i + batch_size]


    def calculate_metric_on_test_ds(self, dataset, metric, model, tokenizer,
                                batch_size=2,
                                column_text="article",
                                column_summary="highlights"):
        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))

        all_predictions = []
        all_references = []

        for article_batch, target_batch in tqdm(
            zip(article_batches, target_batches), total=len(article_batches)):

            inputs = tokenizer(article_batch, max_length=1024,  truncation=True,
                            padding="max_length", return_tensors="pt")

            summaries = model.generate(input_ids=inputs["input_ids"].to(self.device),
                            attention_mask=inputs["attention_mask"].to(self.device),
                            length_penalty=0.8, num_beams=8, max_length=128)

            decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True,
                                    clean_up_tokenization_spaces=True)
                for s in summaries]

            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]

            all_predictions.extend(decoded_summaries)
            all_references.extend(target_batch)

        # Compute and return ROUGE scores
        score = metric.compute(predictions=all_predictions, references=all_references)
        return score
    

    def evaluate(self):
        tokenizer = self.tokenizer
        model = self.model.to(self.device)

        # Load the dataset
        dataset_samsum = load_from_disk(self.config.data_path)

        # Load the metric
        rouge_metric = load("rouge")

        score = self.calculate_metric_on_test_ds(dataset_samsum['test'][0:10], rouge_metric,
                                    model, tokenizer,
                                    batch_size=2,
                                    column_text="dialogue",
                                    column_summary="summary")

        rouge_scores = {key: score[key] for key in ["rouge1", "rouge2", "rougeL", "rougeLsum"]}

        df = pd.DataFrame(rouge_scores, index = [f'pegasus'] )
        df.to_csv(self.config.metric_file_name, index=False)