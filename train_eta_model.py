import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("data/Historical_ticket_data.csv")

# Drop rows with missing values
df = df.dropna(subset=['ticket_text', 'root_cause', 'resolution_time'])

# Feature engineering
df['ticket_length'] = df['ticket_text'].apply(len)

# Encode categorical root cause
encoder = LabelEncoder()
df['root_cause_encoded'] = encoder.fit_transform(df['root_cause'])

# Features and target
X = df[['ticket_length', 'root_cause_encoded']]
y = df['resolution_time']  # this should be in hours

# Train-test split (optional for evaluation)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model and encoder
joblib.dump(model, 'models/eta_model.pkl')
joblib.dump(encoder, 'models/root_cause_encoder.pkl')

print("✅ ETA prediction model saved to 'models/eta_model.pkl'")
