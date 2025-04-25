# import pandas as pd

# splits = {'train': 'synthetic_text_to_sql_train.snappy.parquet', 'test': 'synthetic_text_to_sql_test.snappy.parquet'}
# df = pd.read_parquet("hf://datasets/gretelai/synthetic_text_to_sql/" + splits["train"])


from unsloth import FastLanguageModel
import torch

max_seq_length = 2048
dtype = None
load_in4bit