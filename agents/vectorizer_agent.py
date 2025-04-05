from sentence_transformers import SentenceTransformer
import pickle

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_ticket(text):
    return model.encode(text)

def build_vector_store(ticket_texts, ticket_ids):
    vectors = model.encode(ticket_texts)
    with open("vector_store/vector_index.pkl", "wb") as f:
        pickle.dump((vectors, ticket_ids, ticket_texts), f)
