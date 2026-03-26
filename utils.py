import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python","machine learning","deep learning","data science",
    "sql","java","c++","tensorflow","pandas","numpy","react"
]

def extract_skills(text):
    text = text.lower()
    found = [skill for skill in SKILLS if skill in text]
    return list(set(found))