import streamlit as st

# Set page config
st.set_page_config(
    page_title="AI-Powered Health Companion",
    page_icon="🧬",
    layout="wide"
)

# Hero Section
st.markdown(
    """
    <div style="background: linear-gradient(to right, #2563eb, #7e22ce); padding: 4rem 1rem; text-align: center; color: white; border-radius: 0 0 1rem 1rem;">
        <h1 style="font-size: 3rem; font-weight: bold;">🧬 Your AI-Powered Health Companion</h1>
        <p style="font-size: 1.25rem; max-width: 700px; margin: 1rem auto;">
            Explore tools that combine AI and healthcare to enhance your well-being.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Features Section
st.write("")  # spacing

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🧠 Screen Time & Sanity")
    st.write("Discover how your daily screen usage affects your mental health using intelligent analytics.")
    if st.button("Explore"):
        st.switch_page("views/screen_time_effect.py")

with col2:
    st.markdown("### 🩺 Disease Prediction")
    st.write("Describe your symptoms and get an instant prediction of possible diseases using AI.")
    if st.button("Start Diagnosis"):
        st.switch_page("views/disease_prediction.py")

with col3:
    st.markdown("### 🤖 AI Health Assistant")
    st.write("Chat with your AI-powered medical assistant to get advice and answers in real-time.")
    if st.button("Chat Now"):
        st.switch_page("views/health_bot.py")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>All source code is available on my GitHub under MIT License</p>",
    unsafe_allow_html=True
)
