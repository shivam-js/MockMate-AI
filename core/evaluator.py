import random

def evaluate_full_interview(resume_text, answers):

    full_text = resume_text + " ".join(answers)
    word_count = len(full_text.split())

    # overall score
    if word_count > 200:
        overall = random.randint(80,95)
    elif word_count > 120:
        overall = random.randint(65,80)
    else:
        overall = random.randint(50,65)

    # professional metrics
    technical = random.randint(60,95)
    communication = random.randint(60,95)
    confidence = random.randint(60,95)
    structure = random.randint(60,95)

    feedback = []

    if overall >= 85:
        feedback.append("Excellent interview performance.")
        feedback.append("Strong technical explanations.")
    elif overall >= 70:
        feedback.append("Good answers but add deeper explanations.")
    else:
        feedback.append("Try structuring answers with examples.")

    metrics = {
        "overall": overall,
        "technical": technical,
        "communication": communication,
        "confidence": confidence,
        "structure": structure
    }

    return metrics, feedback
