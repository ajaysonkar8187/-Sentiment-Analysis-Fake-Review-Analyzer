                                              📖 Sentiment & Fake Review Analyzer
A Streamlit web app that analyzes product reviews using a BERT multilingual model, detects fake reviews, and predicts customer behavior (Happy, Unhappy, Neutral).
Supports both English and Hindi reviews via auto-translation.

🚀 Features
🤖 Sentiment Analysis using BERT (1–5 stars rating)

🌐 Auto Language Detection (Hindi/English) with translation

🧠 Customer Behavior Interpretation (Happy, Unhappy, Neutral, etc.)

🔍 Fake Review Detection using simple heuristic rules

🖥️ Interactive UI built with Streamlit

📂 Project Structure
bash
Copy
Edit


sentiment-bert-app/
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignoring venv, pkl, csv files
└── venv/                 # Virtual environment (not uploaded)
🛠️ Tech Stack
Python 3.11

Streamlit – For web app

Transformers (Hugging Face) – Pretrained BERT model

Torch – For model backend

Googletrans – For language detection and translation

📥 Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/sentiment-bert-app.git
cd sentiment-bert-app
Create a Virtual Environment

bash
Copy
Edit
python -m venv venv
.\venv\Scripts\activate
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Streamlit App

bash
Copy
Edit
streamlit run app.py
🧠 How It Works
You enter a review in English or Hindi.

App detects the language and translates if needed.

BERT model predicts review sentiment (1–5 stars).

Based on stars, it classifies customer behavior.

Also detects potential fake reviews using simple rule checks.

🎯 Example Screenshots

Review	Sentiment	Behavior	Fake Review
"Absolutely loved it!"	5 Stars	🥳 Very Happy	✅ Genuine
"Worst product ever."	1 Star	😡 Unhappy	✅ Genuine
"Amazing amazing amazing!"	5 Stars	🥳 Very Happy	⚠️ Possibly Fake
