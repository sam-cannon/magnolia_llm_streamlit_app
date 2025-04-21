import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = "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"  # Replace with your OpenAI API key

st.set_page_config(page_title="ML Chatbot", page_icon="🤖")
st.title("Machine Learning Chatbot")
st.write("Ask me anything about Machine Learning!")

# Chatbot interface
user_input = st.text_input("Enter your question about Machine Learning:")

if user_input:
    try:
        # Query OpenAI's GPT model
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant knowledgeable about machine learning."},
                {"role": "user", "content": user_input},
            ],
        )
        # Extract and display the response
        answer = response["choices"][0]["message"]["content"]
        st.write(f"🤖: {answer}")
    except Exception as e:
        st.error(f"An error occurred: {e}")