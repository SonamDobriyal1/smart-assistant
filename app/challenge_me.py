import random

def generate_questions(text):
    base_questions = [
        "What is the central theme of this document?",
        "List any two insights or findings mentioned.",
        "What conclusion does the author reach?",
        "Mention a challenge or limitation discussed.",
        "Summarize a key section in your own words."
    ]
    return random.sample(base_questions, 3)

def evaluate_answer(user_answer, document_text):
    if user_answer.lower() in document_text.lower():
        return "Good attempt!", "Matched with content in the document."
    else:
        return "Might be off-track.", "Answer does not directly match known content."
