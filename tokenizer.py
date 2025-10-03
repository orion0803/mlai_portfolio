from transformers import AutoTokenizer
# Load tokenizer from a pretrained model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")# Load tokenizer from a pretrained model
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")# Sample text
text = "Transformers are amazing for NLP tasks!"

# Tokenize the text
tokens = tokenizer.tokenize(text)
print("Tokens:", tokens)

# Convert tokens to input IDs
input_ids = tokenizer(text, return_tensors="pt")
print("Input IDs:", input_ids["input_ids"])


