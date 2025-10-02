# mlai_portfolio
# Sentiment Analysis Project

## Environment Setup
- Python 3.10+
- Install dependencies:
  ```bash

# Create an environment:
conda create -n mlai python=3.10

# Change to environment:
conda activate mlai

# Install: pytorch w/ CUDA support
# pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
# Install: pytorch w/o CUDA support
pip install torch torchvision torchaudio

# Install transformers for MML:
pip install transformers datasets accelerate emoji==0.6.0
# Xet Storage
pip install hf_xet
pip install huggingface_hub[hf_xet]
