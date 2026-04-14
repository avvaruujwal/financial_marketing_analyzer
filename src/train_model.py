import os
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

print("Loading dataset...")

# Load dataset
df = pd.read_csv("data/dataset.csv")

# Encode categorical
le = LabelEncoder()
df['Loan'] = le.fit_transform(df['Loan'])

# Split
X = df.drop("Purchased", axis=1)
y = df["Purchased"]

# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Training model...")

# Train classifier
clf = LogisticRegression()
clf.fit(X_scaled, y)

# Train clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_scaled)

print("Saving models...")

# Save models
with open("models/classifier.pkl", "wb") as f:
    pickle.dump(clf, f)

with open("models/clustering.pkl", "wb") as f:
    pickle.dump(kmeans, f)

with open("models/scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Models saved successfully!")