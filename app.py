# import streamlit as st

# # Set page title and layout
# st.set_page_config(page_title="GenAI Powered Aircraft Cabin Design Co-pilot", layout="centered")

# # Add custom CSS for styling (optional, to adjust the button style and layout)
# st.markdown("""
#     <style>
#     .stButton>button {
#         background-color: #e74c3c;
#         color: white;
#         border-radius: 5px;
#         width: 100%;
#         padding: 10px;
#         font-size: 16px;
#     }
#     .stTextInput>div>input {
#         background-color: #f0f0f5;
#     }
#     .title {
#         font-size: 30px;
#         text-align: center;
#         font-weight: bold;
#         margin-bottom: 20px;
#     }
#     .section {
#         margin-bottom: 20px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Title
# st.markdown('<div class="title">GenAI Powered Aircraft Cabin Design Co-pilot</div>', unsafe_allow_html=True)

# # Create two columns for Dimensions and Category
# col1, col2 = st.columns(2)

# # Input for "Dimensions"
# with col1:
#     dimensions = st.text_input("Dimensions", "Passenger Experience")

# # Input for "Category"
# with col2:
#     category = st.text_input("Category", "Seating Arrangement")

# # Text input for the prompt
# prompt = st.text_area("Prompt", "Generate an aircraft cabin image of a modern aircraft where the seating arrangement is optimized to enhance passenger well-being and minimize jet lag.", height=100)

# # Generate button
# if st.button("Generate"):
#     # Here you can add the logic to handle the generation based on the inputs
#     st.success("Generation process started...")


import streamlit as st

# Sample prompts based on clause type
CLAUSE_PROMPTS = {
    "Confidentiality": "Draft a confidentiality clause for a Collaborative Research Agreement. Ensure both parties safeguard shared information.",
    "Termination": "Draft a termination clause that outlines the grounds for terminating a Licensing Agreement.",
    "Liability": "Write a liability clause for a Manufacturing Agreement. Specify limitations and indemnifications for both parties.",
    "Payment Terms": "Create a payment terms clause for a Supply Agreement, specifying timelines and conditions.",
    "Governing Law": "Generate a governing law clause for an Intellectual Property Agreement, specifying jurisdiction."
}

# Options for dropdowns
CATEGORY_OPTIONS = {
    "Select Category": [],
    "Research & Development": ["Collaborative Research", "Sponsored Research"],
    "Licensing": ["In-Licensing", "Out-Licensing"],
    "Manufacturing & Supply": ["Contract Manufacturing", "Supply"],
    "Intellectual Property": ["IP Assignment", "Patent Licensing"],
    "Confidentiality & NDA": ["Sales & Service"]
}

CLAUSE_TYPES = ["Select Clause Type", "Confidentiality", "Termination", "Liability", "Payment Terms", "Governing Law"]

# UI Configuration

st.title("Contract Clause Generator")

# Step 1: Category dropdown
category = st.selectbox("Category", options=["Select Category"] + list(CATEGORY_OPTIONS.keys())[1:])

if category and category != "Select Category":
    # Step 2: Sub-category dropdown appears after category selection
    sub_category = st.selectbox("Sub-category", options=["Select Sub-category"] + CATEGORY_OPTIONS[category])

    if sub_category and sub_category != "Select Sub-category":
        # Step 3: Clause type dropdown appears after sub-category selection
        clause_type = st.selectbox("Clause Type", options=CLAUSE_TYPES)

        if clause_type and clause_type != "Select Clause Type":
            # Step 4: Prompt field appears with the pre-filled text based on clause type
            prompt = CLAUSE_PROMPTS.get(clause_type, "No prompt available for this clause.")
            st.text_area("Prompt", value=prompt, height=150)

# Generate Button
if st.button("Generate"):
    st.success("Generating response for the selected clause... (Integration with LLM pending)")


