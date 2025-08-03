import random
from sentence_transformers import SentenceTransformer, util

def generate_questions(text):
    return [
        "What is the central theme of this document?",
        "List any two insights or findings mentioned.",
        "What conclusion does the author reach?",
        "Mention a challenge or limitation discussed.",
        "Summarize a key section in your own words."
    ]


model = SentenceTransformer('all-MiniLM-L6-v2')

def evaluate_answer(user_answer, document_text, threshold=0.6):
    doc_sentences = [sent.strip() for sent in document_text.split('\n') if len(sent.strip()) > 20]

    embeddings = model.encode([user_answer] + doc_sentences, convert_to_tensor=True)

    user_emb = embeddings[0]
    doc_embs = embeddings[1:]

    cosine_scores = util.pytorch_cos_sim(user_emb, doc_embs)

    max_score = float(cosine_scores.max())

    if max_score >= threshold:
        return "Good attempt!", f"Semantic match found with similarity score: {max_score:.2f}"
    else:
        return "Might be off-track.", f"No close semantic match found. Max similarity: {max_score:.2f}"
