import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Contact Me", page_icon="📬", layout="centered")

# Title Section
st.markdown("""
    <h1 style='text-align: center; color: #4F8BF9;'>📬 Contact Me</h1>
    <p style='text-align: center;'>I'd love to connect! Whether you have a question, opportunity, or just want to say hi.</p>
""", unsafe_allow_html=True)

# Contact Info Section
st.markdown("### 📞 Get in Touch")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📧 Email")
    st.write("sikanderazam276@gmail.com")
    st.markdown("#### ☎️ Phone / WhatsApp")
    st.write("+92 3185836395")

with col2:
    st.markdown("#### 🏠 Address")
    st.write("Ilamabad / Rawalpindi, Pakistan")

# Social Media Section
st.markdown("### 🌐 Connect with Me")

social_links = {
    "Portfolio": "https://azambaltistani.github.io/portfolio/",
    "LinkedIn": "https://www.linkedin.com/in/sikander-azam-899822265/",
    "GitHub": "https://github.com/AzamBaltistani",
    "LeetCode": "https://leetcode.com/u/sikanderazam276/",
    "Facebook": "https://www.facebook.com/s.azam.baltistani"
}

icons = {
    "Portfolio": "❤️",
    "LinkedIn": "🔗",
    "GitHub": "🐙",
    "LeetCode": "💻",
    "Facebook": "📘"
}

cols = st.columns(len(social_links))
for i, (platform, link) in enumerate(social_links.items()):
    with cols[i]:
        st.markdown(
            f"<a href='{link}' target='_blank' style='text-decoration: none;'>"
            f"<div style='text-align:center; font-size: 24px;'>{icons[platform]}</div>"
            f"<div style='text-align:center; font-size: 14px; color: #4F8BF9;'>{platform}</div>"
            f"</a>",
            unsafe_allow_html=True
        )