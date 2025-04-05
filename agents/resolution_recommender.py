from sklearn.metrics.pairwise import cosine_similarity
import pickle

def recommend_resolution(query):
    from agents.vectorizer_agent import embed_ticket
    query_vec = embed_ticket(query)
    with open("vector_store/vector_index.pkl", "rb") as f:
        vectors, ids, texts = pickle.load(f)
    scores = cosine_similarity([query_vec], vectors)[0]
    best_idx = scores.argmax()
    return texts[best_idx], scores[best_idx]
