import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

NVIDIA_BASE_URL = "https://integrate.api.nvidia.com/v1"
NVIDIA_MODEL = "meta/llama-3.1-8b-instruct"

st.set_page_config(page_title="NVIDIA AI Chat Box")
st.title("Simple NVIDIA AI Chat Box")


def get_client():
    api_key = os.getenv("NVIDIA_API_KEY")

    if not api_key:
        st.error("Please add your NVIDIA_API_KEY in the .env file.")
        st.stop()

    return OpenAI(api_key=api_key, base_url=NVIDIA_BASE_URL)


client = get_client()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant for students."}
    ]


for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])


user_question = st.chat_input("Ask something...")

if user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})

    with st.chat_message("user"):
        st.write(user_question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model=NVIDIA_MODEL,
                messages=st.session_state.messages,
            )

            answer = response.choices[0].message.content
            st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
