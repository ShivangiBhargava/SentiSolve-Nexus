import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Load historical ticket data
df = pd.read_csv("data/Historical_ticket_data.csv")
df = df.dropna(subset=["ticket_text"])

# Vectorize ticket text using TF-IDF
vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
X_vectors = vectorizer.fit_transform(df["ticket_text"])

# Build nearest neighbors index (for similarity search)
nn_model = NearestNeighbors(n_neighbors=5, metric='cosine')
nn_model.fit(X_vectors)

# Save vector index and vectorizer
joblib.dump(vectorizer, "vector_store/vectorizer.pkl")
joblib.dump(nn_model, "vector_store/vector_index.pkl")
joblib.dump(df, "vector_store/original_tickets.pkl")  # store ticket text for lookup

print("✅ Vector index and vectorizer saved.")
