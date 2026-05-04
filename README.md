# 📄 AI Resume Analyzer using NLP

🚀 An intelligent web application that analyzes resumes against job descriptions using Natural Language Processing techniques.

---

## 🔍 Features

- 📄 Upload Resume (PDF)
- 📝 Paste Job Description
- 📊 Get Match Score (0–100%)
- 🔑 Identify Missing Keywords
- 💡 Get Resume Improvement Suggestions

---

## 🧠 Tech Stack

- **Python**
- **Streamlit**
- **Scikit-learn**
- **NLP (TF-IDF + Cosine Similarity)**

---

## ⚙️ How It Works

1. Resume is parsed from PDF
2. Text is preprocessed
3. TF-IDF converts text into vectors
4. Cosine similarity computes match score
5. Missing keywords are extracted

---

## 📸 Demo

### 🖥️ Application UI
(Add screenshot here)

---

## ▶️ Run Locally

```bash
git clone https://github.com/your-username/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer
pip install -r requirements.txt
python3 -m streamlit run app.py



📁 Project Structure
AI-Resume-Analyzer/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│
└── src/
    ├── parser.py
    ├── matcher.py
    ├── llm_engine.py



⚠️ Limitations
Keyword-based matching
Limited semantic understanding
Sensitive to wording differences
🚀 Future Improvements
Integration with BERT / LLMs
Semantic similarity detection
Deploy as a web application
👨‍💻 Author

Aman Chaudhary
B.Sc. Data Science & AI
IIT Guwahati




