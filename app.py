import streamlit as st
import google.generativeai as genai

# Configure the Gemini API with your API key
genai.configure(api_key="AIzaSyDqLCF5dbmyFOOBXx5PA4NMmOHOqsTrqQs")

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit app
st.set_page_config(page_title="AI Assistant", page_icon="🤖", layout="centered")

# App title
st.title("AI Assistant")

# Description
st.write("Welcome to the AI Assistant! Ask any question, and I'll do my best to provide a helpful response. Type your query below:")

# User input
user_question = st.text_input("Your Question", placeholder="Type your question here...")

# Generate response when the user submits a question
if st.button("Get Response"):
    if user_question.strip():
        with st.spinner("Generating response..."):
            try:
                # Generate response from Gemini API
                response = model.generate_content(user_question)
                st.success("Response:")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question to get a response.")

# Footer
st.markdown("---")
st.write("Powered by Google Generative AI")