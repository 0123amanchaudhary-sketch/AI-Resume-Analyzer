def get_llm_feedback(resume, jd):
    suggestions = []

    if len(resume) < 300:
        suggestions.append("Resume is too short. Add more content.")

    if "skills" not in resume:
        suggestions.append("Add a skills section.")

    if "project" not in resume:
        suggestions.append("Include project experience.")

    if "experience" not in resume:
        suggestions.append("Mention work experience.")

    if len(suggestions) == 0:
        return "Resume looks good. Try aligning more keywords with job description."

    return " | ".join(suggestions)