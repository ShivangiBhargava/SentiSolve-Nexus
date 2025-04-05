import pickle

def predict_eta(features_dict):
    with open("models/eta_model.pkl", "rb") as f:
        model = pickle.load(f)
    features = [features_dict[k] for k in sorted(features_dict)]
    return round(model.predict([features])[0], 2)
