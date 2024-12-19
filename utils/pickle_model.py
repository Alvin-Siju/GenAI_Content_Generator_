from transformers import GPT2LMHeadModel, GPT2Tokenizer
import pickle

# Load the model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

with open("../model/gpt_model.pkl", "wb") as f:
    pickle.dump((model, tokenizer), f)
