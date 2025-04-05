import pickle

def classify_root_cause(text):
    with open("models/root_cause_model.pkl", "rb") as f:
        model, vectorizer = pickle.load(f)
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]
