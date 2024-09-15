import streamlit as st
import torch
from transformers import AutoTokenizer
from unsloth import FastLanguageModel

# Set page title and layout
st.set_page_config(page_title="GenAI Powered Aircraft Cabin Design Co-pilot", layout="centered")

# Load the LLM and tokenizer
@st.cache_resource(show_spinner=False)
def load_llm():
    max_seq_length = 2048
    dtype = None
    load_in_4bit = True
    
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name="unsloth/Phi-3-mini-4k-instruct",
        max_seq_length=max_seq_length,
        dtype=dtype,
        load_in_4bit=load_in_4bit
    )
    return model, tokenizer

model, tokenizer = load_llm()

# Title
st.markdown('<div class="title">GenAI Powered Aircraft Cabin Design Co-pilot</div>', unsafe_allow_html=True)

# Create two columns for Dimensions and Category
col1, col2 = st.columns(2)

# Input for "Dimensions"
with col1:
    dimensions = st.text_input("Dimensions", "Passenger Experience")

# Input for "Category"
with col2:
    category = st.text_input("Category", "Seating Arrangement")

# Text input for the prompt
prompt = st.text_area("Prompt", "Generate an aircraft cabin image of a modern aircraft where the seating arrangement is optimized to enhance passenger well-being and minimize jet lag.", height=100)

# Alpaca-style prompt formatting
alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

# Generate button
if st.button("Generate"):
    # Combine the instruction and input into a formatted prompt for the LLM
    input_text = alpaca_prompt.format(dimensions, category, prompt)

    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt", padding=True, truncation=True).to("cuda")

    # Generation parameters
    generation_params = {
        "max_new_tokens": 5000,
        "do_sample": True,
        "temperature": 0.8,
    }

    # Generate the response from the LLM
    generated_ids = model.generate(**inputs, **generation_params)
    generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    # Display the generated response
    st.subheader("Generated Response")
    st.write(generated_text)
