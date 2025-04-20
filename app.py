import streamlit as st

st.set_page_config(page_title="My Streamlit App", page_icon="🚀")
st.title("Welcome to My Streamlit App")
st.write("This is an interactive app embedded in a Wix webpage!")

# Example widget
value = st.slider("Select a value", 0, 100, 50)
st.write(f"Selected value squared is: {value * value}")