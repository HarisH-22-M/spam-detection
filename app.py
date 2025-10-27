import streamlit as st
import joblib
import re

@st.cache_resource
def load_model(path="email_updated.joblib"):
    return joblib.load(path)

model = load_model()

def clean_text(s):
    if not s: return ""
    s = s.lower()
    s = re.sub(r'http\S+|www\S+', '', s)
    s = re.sub(r'\S+@\S+', '', s)
    s = re.sub(r'[^a-z0-9\s]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

st.title("📧 Gmail / SMS Spam Detector")

user_input = st.text_area("Paste your email or SMS content here:", height=300)

if st.button("Check"):
    cleaned = clean_text(user_input)
    pred = model.predict([cleaned])[0]
    prob = model.predict_proba([cleaned])[0][1]
    
    if pred == 1:
        st.error(f"🚨 Spam Detected! (Probability: {prob:.2%})")
    else:
        st.success(f"✅ Not Spam (Probability: {prob:.2%})")
