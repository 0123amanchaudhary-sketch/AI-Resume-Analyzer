import streamlit as st
from src.parser import extract_text_from_pdf
from src.matcher import get_similarity_score, get_missing_keywords
from src.llm_engine import get_llm_feedback

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if uploaded_file and job_description:
        resume_text = extract_text_from_pdf(uploaded_file)

        score = get_similarity_score(resume_text, job_description)
        missing = get_missing_keywords(resume_text, job_description)
        feedback = get_llm_feedback(resume_text, job_description)

        st.write("Match Score:", round(score*100, 2), "%")
        st.write("Missing Keywords:", missing)
        st.write("Suggestions:", feedback)
    else:
        st.write("Please upload resume and enter job description")

        