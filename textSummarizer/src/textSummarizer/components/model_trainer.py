import os
import torch
from transformers import (AutoModelForSeq2SeqLM, AutoTokenizer, 
                            Trainer, TrainingArguments, DataCollatorForSeq2Seq)
from datasets import load_from_disk
from textSummarizer.entity import TrainerConfig


class ModelTrainer:
    def __init__(self, config: TrainerConfig):
        self.config = config
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(self.device)
        self.dataCollator = DataCollatorForSeq2Seq(tokenizer=self.tokenizer,
                                                    model=self.model,)
        

    def train(self):
        # Load dataset
        dataset = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir, 
            num_train_epochs=self.config.num_train_epochs, 
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size, 
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            weight_decay=self.config.weight_decay, 
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy, 
            eval_steps=self.config.eval_steps, 
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        ) 

        trainer = Trainer(model=self.model, args=trainer_args,
                  tokenizer=self.tokenizer, data_collator=self.dataCollator,
                  train_dataset=dataset["train"], 
                  eval_dataset=dataset["validation"],)
        
        trainer.train()

        # Save the model
        self.model.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        self.tokenizer.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-tokenizer"))