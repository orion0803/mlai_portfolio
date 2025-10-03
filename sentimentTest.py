# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("-------------------------------")
print("-------------------------------")
print("-------------------------------")

# checking environment
import sys
print(sys.executable)

print("--------- PYTORCH ------------")
# simple pytorch example
#import torch
#x = torch.rand(5, 3)
#print(x)

print("--------- LLM Transformer ------------")
# simple LLM example
import logging
import warnings
from transformers import pipeline

# Suppress warnings
warnings.filterwarnings("ignore")
# Suppress transformers and other library logs
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("torch").setLevel(logging.ERROR)
logging.getLogger().setLevel(logging.ERROR)  # Catch-all

#classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment") #label # of stars
classifier = pipeline("sentiment-analysis", model="finiteautomata/bertweet-base-sentiment-analysis") #label pos or neg or neu

#statement = "I've been waiting for a HuggingFace course my whole life."
statement = input("Enter a statement for a sentiment analysis: ")
result = classifier(statement);
print(result)
print("score: ", result[0].get("score"))
score = result[0].get("score")
label = result[0].get("label")

print("Your statement was ", label)
# if score > 0.65:
#     print("Possitive statement!")
# elif score > 0.35:
#     print("meh statement")
# else:
#     print("Negative statement!")

print("--------- Finished ------------")
