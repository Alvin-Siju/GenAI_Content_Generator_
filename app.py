import streamlit as st
from utils.generate_content import preprocess_prompt  # Import the function to generate content

# Streamlit app
st.title("AI-based Content Generation Platform")

# Text area for user input
user_input = st.text_area("Enter a topic or prompt for content generation:")

# Button to trigger content generation
if st.button("Generate Content"):
    if user_input:
        try:
            generated_text = preprocess_prompt(user_input)
            st.write("Generated Content:")
            st.write(generated_text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a topic or prompt.")
