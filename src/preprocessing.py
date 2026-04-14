import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess(path):
    df = pd.read_csv(path)

    # Encode categorical data
    le = LabelEncoder()
    if 'Loan' in df.columns:
        df['Loan'] = le.fit_transform(df['Loan'])

    # Split features and target
    X = df.drop('Purchased', axis=1)
    y = df['Purchased']

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler