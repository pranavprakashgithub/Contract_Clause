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




# import streamlit as st

# # Sample prompts based on clause type
# CLAUSE_PROMPTS = {
#     "Confidentiality": "Draft a confidentiality clause for a Collaborative Research Agreement. Ensure both parties safeguard shared information.",
#     "Termination": "Draft a termination clause that outlines the grounds for terminating a Licensing Agreement.",
#     "Liability": "Write a liability clause for a Manufacturing Agreement. Specify limitations and indemnifications for both parties.",
#     "Payment Terms": "Create a payment terms clause for a Supply Agreement, specifying timelines and conditions.",
#     "Governing Law": "Generate a governing law clause for an Intellectual Property Agreement, specifying jurisdiction."
# }

# # Options for dropdowns
# CATEGORY_OPTIONS = {
#     "Select Category": [],
#     "Research & Development": ["Collaborative Research", "Sponsored Research"],
#     "Licensing": ["In-Licensing", "Out-Licensing"],
#     "Manufacturing & Supply": ["Contract Manufacturing", "Supply"],
#     "Intellectual Property": ["IP Assignment", "Patent Licensing"],
#     "Confidentiality & NDA": ["Sales & Service"]
# }

# CLAUSE_TYPES = ["Select Clause Type", "Confidentiality", "Termination", "Liability", "Payment Terms", "Governing Law"]

# # UI Configuration

# st.title("Contract Clause Generator")

# # Step 1: Category dropdown
# category = st.selectbox("Category", options=["Select Category"] + list(CATEGORY_OPTIONS.keys())[1:])

# if category and category != "Select Category":
#     # Step 2: Sub-category dropdown appears after category selection
#     sub_category = st.selectbox("Sub-category", options=["Select Sub-category"] + CATEGORY_OPTIONS[category])

#     if sub_category and sub_category != "Select Sub-category":
#         # Step 3: Clause type dropdown appears after sub-category selection
#         clause_type = st.selectbox("Clause Type", options=CLAUSE_TYPES)

#         if clause_type and clause_type != "Select Clause Type":
#             # Step 4: Prompt field appears with the pre-filled text based on clause type
#             prompt = CLAUSE_PROMPTS.get(clause_type, "No prompt available for this clause.")
#             st.text_area("Prompt", value=prompt, height=150)

# # Generate Button
# if st.button("Generate"):
#     st.success("Generating response for the selected clause... (Integration with LLM pending)")





# import streamlit as st
# import os
# import torch

# # Force torch to use CPU
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# torch.device('cpu')

# # Monkey-patch unsloth to bypass the CUDA check
# import torch.cuda

# def no_cuda():
#     return False

# torch.cuda.is_available = no_cuda
# torch.cuda.get_device_capability = lambda: (0, 0)

# from unsloth import FastLanguageModel

# # Now proceed with loading the model as usual
# model = FastLanguageModel()

# # Continue with your application code

# # Set page configuration and title
# st.set_page_config(page_title="Contract Clause Generator", layout="centered")

# # Custom CSS for styling the box and button
# st.markdown("""
#     <style>
#     .box {
#         background-color: #f0f0f5;
#         padding: 20px;
#         border-radius: 10px;
#         margin-bottom: 20px;
#     }
#     .button-container {
#         display: flex;
#         justify-content: center;
#         margin-top: 20px;
#     }
#     .full-width-button {
#         width: 100%;
#         background-color: #ff4b4b;
#         color: white;
#         font-size: 18px;
#         padding: 12px;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Title
# st.title("Contract Clause Generator")

# # Container for dropdowns and prompt
# with st.container():
#     st.markdown("<div class='box'>", unsafe_allow_html=True)
    
#     # Category and Sub-category in the same line
#     col1, col2 = st.columns(2)
    
#     category = col1.selectbox("Category", [
#         "Select Category", "Research & Development", "Licensing", "Manufacturing & Supply", 
#         "Intellectual Property", "Confidentiality and Non-disclosure"
#     ])
    
#     # Sub-category logic based on category selection
#     sub_category_options = {
#         "Research & Development": ["Collaborative Research", "Sponsored Research"],
#         "Licensing": ["In-Licensing", "Out-Licensing"],
#         "Manufacturing & Supply": ["Contract Manufacturing", "Supply"],
#         "Intellectual Property": ["IP Assignment", "Patent Licensing"],
#         "Confidentiality and Non-disclosure": ["Sales & Service"],
#     }
    
#     if category != "Select Category":
#         sub_category = col2.selectbox("Sub-category", ["Select Sub-category"] + sub_category_options[category])
#     else:
#         sub_category = col2.selectbox("Sub-category", ["Select Sub-category"])

#     # Clause type dropdown
#     if sub_category != "Select Sub-category":
#         clause_type = st.selectbox("Clause Type", [
#             "Select Clause", "Confidentiality", "Termination", "Liability", 
#             "Payment Terms", "Governing Law"
#         ])
#     else:
#         clause_type = st.selectbox("Clause Type", ["Select Clause"])
    
#     # Prompt field appears after clause is selected
#     if clause_type != "Select Clause":
#         prompt = f"Generate a {clause_type} clause based on {sub_category} in {category}."
#         st.text_area("Prompt", value=prompt, height=150)
    
#     st.markdown("</div>", unsafe_allow_html=True)

# # File uploader and validate button
# with st.container():
#     st.file_uploader("Upload a document for validation", type=["txt", "pdf", "docx"])

#     st.markdown("<div class='button-container'>", unsafe_allow_html=True)
#     st.button("Validate", key="validate_button")
#     st.markdown("</div>", unsafe_allow_html=True)

# # Generate button centered below the form
# st.markdown("<div class='button-container'>", unsafe_allow_html=True)
# if st.button("Generate", key="generate_button"):
#     # Placeholder LLM integration
#     st.success("LLM output generated! (LLM integration will be connected here)")
# st.markdown("</div>", unsafe_allow_html=True)






import streamlit as st

# Define category, sub-category, and clause type options
categories = {
    "Research & Development": ["Collaborative Research", "Sponsored Research"],
    "Licensing": ["In-Licensing", "Out-Licensing"],
    "Manufacturing & Supply": ["Contract Manufacturing", "Supply"],
    "Intellectual Property": ["IP Assignment", "Patent Licensing"],
    "Confidentiality & NDA": ["Sales & Service"]
}

clause_types = ["Confidentiality", "Termination", "Liability", "Payment Terms", "Governing Law"]

# Create Streamlit app
def main():
    st.title("Contract Clause Generator")

    # Apply custom CSS for box structure, background colors, and button styling
    st.markdown("""
    <style>
    .main {
        background-color: #1a1a1a; /* Page background close to black */
    }
    .box {
        background-color: #001f3f; /* Navy blue form field background */
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #ccc;
        margin-bottom: 20px;
    }
    .stTextArea textarea {
        font-family: Arial, sans-serif;
        font-size: 14px;
        color: #333;
        background-color: #f5f5f5;
        border: 1px solid #ccc;
        padding: 10px;
        width: 100%;
    }
    .stButton button {
        background-color: #ff4136; /* Red button background */
        color: white; /* White button text */
        width: 100%; /* Full width of form fields */
        padding: 10px;
        font-size: 16px;
        border-radius: 5px;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

    # Start of the box structure
    with st.container():
        st.markdown('<div class="box">', unsafe_allow_html=True)

        # Category and Sub-category on the same line
        col1, col2 = st.columns(2)
        with col1:
            category = st.selectbox("Category", ["Select Category"] + list(categories.keys()))
        with col2:
            sub_category = st.selectbox("Sub-Category", ["Select Sub-Category"] + categories.get(category, []))

        # Clause type dropdown
        if sub_category != "Select Sub-Category":
            clause_type = st.selectbox("Clause Type", ["Select Clause Type"] + clause_types)
        else:
            clause_type = "Select Clause Type"

        # Display prompt field after Clause Type selection
        if clause_type != "Select Clause Type":
            prompt_text = f"Generate a contract clause for {category} -> {sub_category} -> {clause_type}."
            st.text_area("Prompt", value=prompt_text, height=80)  # Adjusted height to match content

        # Generate button
        if st.button("Generate"):
            # Placeholder logic for clause generation
            generated_clause = "Generated clause based on the selected options."
            st.text_area("Generated Clause", value=generated_clause, height=200)

        st.markdown('</div>', unsafe_allow_html=True)  # End of the box

    # Document upload section outside the box
    with st.container():
        uploaded_file = st.file_uploader("Upload Document")
        if st.button("Validate"):
            if uploaded_file is not None:
                st.success("Document validated successfully!")
            else:
                st.warning("Please upload a document.")

if __name__ == "__main__":
    main()
