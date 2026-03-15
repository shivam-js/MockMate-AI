import random
import re

# professional followup templates
FOLLOWUP_TEMPLATES = [
    "Can you explain more about how you implemented {}?",
    "What challenges did you face while working with {}?",
    "How did you measure the success of your work using {}?",
    "What improvements would you make if you rebuilt this using {}?",
    "Why did you choose {} instead of other approaches?",
    "What was the most difficult part when using {}?",
]


def extract_keywords(answer):

    words = re.findall(r'\b[a-zA-Z]{4,}\b', answer.lower())

    stopwords = {
        "this","that","with","from","have","there","their",
        "about","which","when","where","while","would",
        "could","should","your","using","used","into",
        "were","been","they","them"
    }

    keywords = [w for w in words if w not in stopwords]

    return list(set(keywords))


def generate_followup(answer, skills):

    keywords = extract_keywords(answer)

    # priority 1 → keywords from answer
    if keywords:
        topic = random.choice(keywords)

    # priority 2 → resume skills
    elif skills:
        topic = random.choice(skills)

    # fallback
    else:
        topic = "this project"

    template = random.choice(FOLLOWUP_TEMPLATES)

    question = template.format(topic)

    return question
