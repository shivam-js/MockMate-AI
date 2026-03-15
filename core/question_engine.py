import random

def generate_questions(skills):

    questions = []

    for skill in skills:

        questions.append(f"Explain your experience with {skill}.")
        questions.append(f"What challenges did you face while using {skill}?")
        questions.append(f"Describe a project where you used {skill}.")

    random.shuffle(questions)

    return questions[:5]