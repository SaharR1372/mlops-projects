import streamlit as st 
import pandas as pd
import numpy as np

# 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
# st.write("Hello, Streamlit!")
# 'hello world'

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# })
# st.write(df)

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon']
# )
# st.map(map_data)

# st.text_input("Your name", key="name")
# st.session_state.name  # u an access the value at any point with st.session_state

# st.title("My first app")

import os
import requests
API_KEY=st.secrets["API_KEY"]
API_URL = "https://router.huggingface.co/hf-inference/models/valhalla/distilbart-mnli-12-3"
headers = {
    "Authorization": f"Bearer {API_KEY}",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

labels=st.multiselect("chose your labels", ["refund", "legal", "faq"])
inputs=st.text_input("Enter your text", "Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!")
output = query({
    "inputs": inputs,
    "parameters": {"candidate_labels": labels},
})
output