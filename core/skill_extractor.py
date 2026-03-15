def extract_skills(text):

    skills = [
        "python","machine learning","nlp",
        "sql","streamlit","javascript",
        "html","css"
    ]

    found = []

    for s in skills:
        if s in text.lower():
            found.append(s)

    return list(set(found))