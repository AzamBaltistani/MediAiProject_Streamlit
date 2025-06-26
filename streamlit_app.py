import streamlit as st

pages = st.navigation(
    [
        st.Page(
            page="views/home_page.py",
            title="Home",
            default=True  
        ),
        st.Page(
            page="views/screen_time_effect.py",
            title="Screen Time & Sanity",
            url_path="Screen_Time_Effect"
        ),
        st.Page(
            page="views/disease_prediction.py",
            title="Disease Prediction",
            url_path="Disease_Prediction"
        ),
        st.Page(
            page="views/health_bot.py",
            title="AI Health Assistant",
            url_path="Health_Chatbot"
        ),
        st.Page(
            page="views/contact_me.py",
            title="Contact Me",
            url_path="Contact_Me"
        )
    ]
)

pages.run()