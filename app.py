import streamlit as st

# Set page title and layout
st.set_page_config(page_title="GenAI Powered Aircraft Cabin Design Co-pilot", layout="centered")

# Add custom CSS for styling (optional, to adjust the button style and layout)
st.markdown("""
    <style>
    .stButton>button {
        background-color: #e74c3c;
        color: white;
        border-radius: 5px;
        width: 100%;
        padding: 10px;
        font-size: 16px;
    }
    .stTextInput>div>input {
        background-color: #f0f0f5;
    }
    .title {
        font-size: 30px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .section {
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

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

# Generate button
if st.button("Generate"):
    # Here you can add the logic to handle the generation based on the inputs
    st.success("Generation process started...")

