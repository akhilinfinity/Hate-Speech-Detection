import streamlit as st
import joblib
import re
import string

# Load your trained model and vectorizer
model = joblib.load("hate_speech_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)  # remove links
    text = re.sub(r'@\w+', '', text)     # remove mentions
    text = re.sub(r'#\w+', '', text)     # remove hashtags
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    return text

# Streamlit UI
st.title("Hate Speech Detection App")
st.write("Classifies text as **Hate Speech**, **Offensive Language**, or **Neutral**.")

user_input = st.text_area("Enter your text here:")

if st.button("Predict"):
    if user_input.strip() != "":
        cleaned_text = clean_text(user_input)
        vectorized_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized_text)[0]

        labels = {0: "Hate Speech", 1: "Offensive Language", 2: "Neutral"}
        st.write(f"**Prediction:** {labels[prediction]}")
    else:
        st.warning("Please enter some text.")
