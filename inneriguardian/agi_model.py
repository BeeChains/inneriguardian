import openai
#import bittensor
import requests
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# Load AI Models
o3_mini = AutoModelForCausalLM.from_pretrained("InnerI/InnerI-bittensor-7b")
tokenizer = AutoTokenizer.from_pretrained("InnerI/InnerI-bittensor-7b")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BITTENSOR_WALLET = os.getenv("BITTENSOR_WALLET")

def query_agi(input_text):
    """ Calls multiple AI APIs (GPT-4, Bittensor, O3-mini, OL) """
    
    # GPT-4 API
    gpt_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": input_text}],
        api_key=OPENAI_API_KEY
    )["choices"][0]["message"]["content"]
    
    # Bittensor AI Response
    bt_response = bittensor.Wallet().send(input_text)

    # O3-mini Response
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    o3_response = tokenizer.decode(o3_mini.generate(input_ids, max_length=100)[0])

    # Return AI response
    return {
        "GPT-4": gpt_response,
        "Bittensor": bt_response,
        "O3-mini": o3_response
    }
