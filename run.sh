#!/bin/bash

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Notify user
echo "Setup complete. Run your Jupyter notebook or Streamlit app manually."