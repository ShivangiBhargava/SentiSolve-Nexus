import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

# Load historical data
df = pd.read_csv("data/Historical_ticket_data.csv")

# Basic cleanup
df = df.dropna(subset=['ticket_text', 'root_cause'])

# Define features and labels
X = df['ticket_text']
y = df['root_cause']

# Create pipeline: TF-IDF + Logistic Regression
model = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=1000)),
    ('clf', LogisticRegression(max_iter=1000))
])

# Train the model
model.fit(X, y)

# Save the model
joblib.dump(model, 'models/root_cause_model.pkl')

print("✅ Root cause classification model saved to 'models/root_cause_model.pkl'")
