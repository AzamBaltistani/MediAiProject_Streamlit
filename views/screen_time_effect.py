import streamlit as st
import numpy as np
import joblib
import plotly.graph_objects as go
import os

@st.cache_resource
def load_model(path):
    return joblib.load(path)

path = os.getcwd() + "/views/trained_models/health_impact/mental_health_model_MOXGReg.pkl"
model = load_model(path)

max_vals = {
    "screen_time_hours": 12.0,
    "social_media_platforms_used": 5,
    "hours_on_TikTok": 7.2,
    "sleep_hours": 10.0
}

st.set_page_config(page_title="Screen Time & Sanity", layout="wide")
st.title("Screen Time Impact on Mental Health")

left_col, right_col = st.columns([2, 1])

with left_col:
    screen_time = st.slider("📱 Screen Time (hours)", 0.0, max_vals["screen_time_hours"], 6.0, 0.1)
    platforms_used = st.slider("🌐 Social Media Platforms Used", 0, max_vals["social_media_platforms_used"], 3)
    tiktok_hours = st.slider("🎵 Hours on TikTok", 0.0, max_vals["hours_on_TikTok"], 2.0, 0.1)
    sleep_hours = st.slider("🛌 Sleep Hours", 0.0, max_vals["sleep_hours"], 7.0, 0.1)

    # Predict
    input_data = np.array([[screen_time, platforms_used, tiktok_hours, sleep_hours]])
    prediction = model.predict(input_data)
    stress = round(prediction[0][0], 2)
    mood = round(prediction[0][1], 2)

with right_col:
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=["Stress Level"],
        y=[stress],
        name="Stress Level",
        marker_color='crimson',
        text=f"{stress:.2f}/10",
        textposition='auto'
    ))

    fig.add_trace(go.Bar(
        x=["Mood Score"],
        y=[mood],
        name="Mood Score",
        marker_color='mediumseagreen',
        text=f"{mood:.2f}/10",
        textposition='auto'
    ))

    fig.update_layout(
        yaxis=dict(range=[0, 10]),
        barmode='group',
        template='plotly_white',
        height=400,
    )

    st.plotly_chart(fig, use_container_width=True)
st.markdown(f"🧪 **Stress Level**: `{stress:.2f}` / 10")
st.markdown(f"😊 **Mood Score**: `{mood:.2f}` / 10")
