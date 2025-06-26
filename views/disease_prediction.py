import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Layer
from tensorflow.keras import backend as K
from tensorflow.keras.utils import custom_object_scope
from tensorflow.keras.saving import register_keras_serializable
import numpy as np
import pickle
import re
import os
import random

# ---- Custom Attention Layer ----
@register_keras_serializable(package="Custom")
class AttentionLayer(Layer):
    def build(self, input_shape):
        self.W = self.add_weight(name="att_weight", shape=(input_shape[-1], 1), initializer="normal")
        self.b = self.add_weight(name="att_bias", shape=(input_shape[1], 1), initializer="zeros")
        super().build(input_shape)

    def call(self, inputs):
        e = K.tanh(K.dot(inputs, self.W) + self.b)
        a = K.softmax(e, axis=1)
        output = inputs * a
        return K.sum(output, axis=1)

# ---- Example Symptoms ----
symptom_examples = [
    "The skin around my mouth, nose, and eyes is red and inflamed. It is often itchy and uncomfortable. There is a noticeable inflammation in my nails.",
    "The swelling in my legs is causing me to have difficulty fitting into my shoes...",
    "I have constipation and belly pain, and it's been really uncomfortable...",
    "I'm feeling fatigued and have no energy. I can barely keep my eyes open...",
    "The sores on my face are beginning to weep clear fluid. Also, every night...",
    "I have been experiencing chills and shivering. There is a strong pain in my back...",
    "My skin has been itching a lot and developing a rash...",
    "My eyes are always red and itchy, and my nose feels all stuffy...",
    "I've had a terrible cough and cold for days...",
    "I'm having a lot of trouble breathing and am really uneasy...",
    "I've been having a lot of trouble with my bowel movements lately...",
    "Recently, when I try to walk about, I have stiffness, a stiff neck...",
    "When I awoke this morning, I saw a severe rash across my skin...",
    "I've been experiencing terrible itching and nausea. I've lost weight..."
]

# ---- Text Cleaning ----
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# ---- Model Loading Function ----
@st.cache_resource
def load_model_and_utils():
    base_path = os.getcwd()
    model_path = os.path.join(base_path, "views/trained_models/disease_prediction/disease_prediction_model.keras")
    tokenizer_path = os.path.join(base_path, "views/trained_models/disease_prediction/tokenizer.pkl")
    label_encoder_path = os.path.join(base_path, "views/trained_models/disease_prediction/label_encoder.pkl")

    with st.spinner("🔄 Loading model and tools..."):
        with custom_object_scope({"AttentionLayer": AttentionLayer}):
            model = load_model(model_path, compile=False)
        tokenizer = pickle.load(open(tokenizer_path, "rb"))
        label_encoder = pickle.load(open(label_encoder_path, "rb"))
    return model, tokenizer, label_encoder

# ---- Streamlit UI ----
st.set_page_config(page_title="Disease Predictor", layout="centered")
st.title("🩺 Disease Prediction from Symptoms")
st.markdown("Enter your symptoms in plain language to get a predicted disease.")

if "example_text" not in st.session_state:
    st.session_state.example_text = ""

# ---- Text Area ----
user_input = st.text_area("📝 Enter symptoms", value=st.session_state.example_text, height=150)

# ---- Button Row (Random + Predict) ----
col1, col2 = st.columns([1, 2])
with col1:
    if st.button("🎲 Random Example"):
        st.session_state.example_text = random.choice(symptom_examples)
        st.rerun()

with col2:
    if st.button("🔍 Predict Disease"):
        if user_input.strip() == "":
            st.warning("Please enter symptoms to predict.")
        else:
            # Load model with visible spinner animation
            model, tokenizer, label_encoder = load_model_and_utils()

            cleaned = clean_text(user_input)
            seq = tokenizer.texts_to_sequences([cleaned])
            padded = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=100, padding='post')

            with st.spinner("🧠 Making prediction..."):
                prediction = model.predict(padded)
                predicted_label = label_encoder.inverse_transform([np.argmax(prediction)])[0]

            st.success(f"🧾 **Predicted Disease:** `{predicted_label}`")
