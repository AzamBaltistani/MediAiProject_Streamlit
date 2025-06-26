import streamlit as st
from google import genai
import time

st.set_page_config(page_title="Medi Health Chatbot", page_icon="🤖")

try:
    gemini_api_key = st.secrets["GEMINI_API_KEY"]
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY environment variable is not set.")
except (KeyError, ValueError) as e:
    st.error(f"Error loading API Key")
    st.stop()

if "genai_client" not in st.session_state:
    try:
        st.session_state.genai_client = genai.Client(api_key=gemini_api_key)
    except Exception as e:
        st.error(f"Failed to initialize GenAI client: {e}")
        st.stop()

if "chat_session" not in st.session_state:
    try:
        st.session_state.chat_session = st.session_state.genai_client.chats.create(model="gemini-1.5-flash")
    except Exception as e:
        st.error(f"Failed to create chat session: {e}")
        st.stop()

# --- Streamlit UI Setup ---
st.title("Medi Health Chatbot")

for message in st.session_state.chat_session.get_history():
    # The role is accessed via message.role, and content via message.parts[0].text
    with st.chat_message(message.role):
        st.markdown(message.parts[0].text)

# --- User Input ---
user_prompt = st.chat_input("Ask you problem to our powerfull chatbot ...")

if user_prompt:
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            stream = st.session_state.chat_session.send_message_stream(user_prompt)

            for chunk in stream:
                full_response += chunk.text
                message_placeholder.markdown(full_response + "▌")
                time.sleep(0.1)

            message_placeholder.markdown(full_response)

        except Exception as e:
            st.error(f"An error occurred: {e}. Please try again.")