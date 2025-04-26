import streamlit as st
from transformers import pipeline
from googletrans import Translator
import re

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(page_title="Sentiment & Behavior Analyzer", page_icon="🤖")

# -------------------------------
# Load BERT Sentiment Model
# -------------------------------
@st.cache_resource
def load_sentiment_pipeline():
    return pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

sentiment_pipeline = load_sentiment_pipeline()
translator = Translator()

# -------------------------------
# Heuristic for Fake Review Detection
# -------------------------------
def is_fake_review(text):
    if len(text.split()) < 5 or re.search(r"(amazing|awesome|perfect|great){2,}", text.lower()):
        return "⚠️ Possibly Fake"
    return "✅ Genuine"

# -------------------------------
# Map Stars to Customer Behavior
# -------------------------------
def interpret_behavior(label):
    star = int(label[0])  # extract star number from label like '5 stars'
    if star == 1:
        return "😡 Unhappy"
    elif star == 2:
        return "😕 Dissatisfied"
    elif star == 3:
        return "😐 Neutral"
    elif star == 4:
        return "🙂 Happy"
    else:
        return "🥳 Very Happy"

# -------------------------------
# Streamlit UI Layout
# -------------------------------
st.title("🤖 Sentiment, Fake Review & Behavior Analyzer")
st.markdown("Analyze customer product reviews using **BERT**, **language detection**, and **fake review detection**.")

# Text Input
review = st.text_area("📝 Enter your product review (English or Hindi):")

# Button
if st.button("Analyze"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        # Detect and translate language
        detected_lang = translator.detect(review).lang
        st.write("🌐 **Detected Language:**", detected_lang.upper())

        if detected_lang != "en":
            translated = translator.translate(review, src=detected_lang, dest='en').text
            st.write("🔁 **Translated Review:**", translated)
            input_text = translated
        else:
            input_text = review

        # Sentiment Analysis
        result = sentiment_pipeline(input_text)[0]
        label = result['label']
        score = result['score']
        st.subheader("📊 Sentiment Result")
        st.success(f"**Label**: {label} \n**Confidence**: {score:.2f}")

        # Customer Behavior
        behavior = interpret_behavior(label)
        st.subheader("🧠 Customer Behavior")
        st.info(f"Behavior Based on Review: **{behavior}**")

        # Fake Review Detection
        authenticity = is_fake_review(input_text)
        st.subheader("🕵️ Fake Review Check")
        if "Fake" in authenticity:
            st.warning(authenticity)
        else:
            st.info(authenticity)



