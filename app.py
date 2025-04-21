import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

# Load model and tokenizer
@st.cache_resource
def load_model():
    model_name = "tiiuae/falcon-rw-1b"  # small model for local CPU/GPU
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)
    return pipe

st.title("💬 Simple Chat with Lightweight LLM")
pipe = load_model()

# User input
user_input = st.text_input("You:", "")

# Chat history (could also use session_state for persistent history)
if "history" not in st.session_state:
    st.session_state.history = []

if user_input:
    # Build prompt with history (optional)
    prompt = ""
    for role, message in st.session_state.history:
        prompt += f"{role}: {message}\n"
    prompt += f"You: {user_input}\nLLM:"

    # Generate reply
    with st.spinner("Thinking..."):
        response = pipe(prompt, max_new_tokens=100, do_sample=True, temperature=0.7)[0]['generated_text']
        reply = response.split("LLM:")[-1].strip()

    # Store in history
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("LLM", reply))

# Display history
for role, message in st.session_state.history:
    st.markdown(f"**{role}**: {message}")
