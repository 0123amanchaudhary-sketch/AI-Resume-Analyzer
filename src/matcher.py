from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity_score(resume, jd):
    tfidf = TfidfVectorizer(stop_words='english')
    vectors = tfidf.fit_transform([resume, jd])
    score = cosine_similarity(vectors[0:1], vectors[1:2])
    return score[0][0]

def get_missing_keywords(resume, jd):
    jd_words = set(jd.lower().split())
    resume_words = set(resume.lower().split())
    missing = jd_words - resume_words
    return list(missing)[:20]

    