import os
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer
import transformers
import torch
from transformers import AutoTokenizer
import streamlit as st

# The following codes are adjusted for use with GROQ and HF.

# import tiktoken

# un-comment when in vs-code
# load_dotenv('.env')
# client = Groq(api_key=os.getenv('GROQ_KEY'))

# for streamlit
client = Groq(
    api_key=st.secrets["GROQ_KEY"],)

def get_embeddings(input, model='sentence-transformers/all-mpnet-base-v2'):
    model = SentenceTransformer(model)
    # model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
    embeddings = model.encode(input)
    print(embeddings)
    return [x for x in embeddings.data]

# This is the "Updated" helper function for calling LLM
def get_completion(prompt, model="llama-3.1-70b-versatile", temperature=0, top_p=1.0, max_tokens=256, n=1, json_output=False):
    if json_output == True:
      output_json_structure = {"type": "json_object"}
    else:
      output_json_structure = None

    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create( #originally was openai.chat.completions
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=1,
        response_format=output_json_structure,
    )
    return response.choices[0].message.content

# Note that this function directly take in "messages" as the parameter.
def get_completion_by_messages(messages, model="llama-3.1-70b-versatile", temperature=0, top_p=1.0, max_tokens=1024, n=1):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
        n=1
    )
    return response.choices[0].message.content

# This function is for calculating the tokens given the "message"
# ⚠️ This is simplified implementation that is good enough for a rough estimation

# unhide when in vs code
# access_token = os.getenv('HF_KEY')

access_token = st.secrets["HF_KEY"]

# included above
# import transformers
# import torch
model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

pipeline = transformers.pipeline(
"text-generation",
model=model_id,
model_kwargs={"torch_dtype": torch.bfloat16},
token=access_token,
device_map="auto",
)


# included above
# from transformers import AutoTokenizer
def count_tokens(text):
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3.1-8B-Instruct")
    tokens = tokenizer.tokenize(text)
    num_tokens = len(tokens)
    return num_tokens

def num_tokens_from_message_rough(messages):
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3.1-8B-Instruct")
    tokens = tokenizer.tokenize(messages)
    num_tokens = len(tokens)
    print(f"Number of tokens in your text: {num_tokens}")
    return num_tokens
