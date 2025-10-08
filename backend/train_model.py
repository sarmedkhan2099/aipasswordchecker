import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import re

# Example dataset
data = pd.DataFrame({
    'password': ['123456', 'Password123!', 'abc', 'StrongPass!9'],
    'strength': [0, 2, 0, 2]  # 0=weak, 2=strong
})

# Feature extraction
data['length'] = data['password'].apply(len)
data['digits'] = data['password'].str.count(r'\d')
data['special'] = data['password'].str.count(r'[!@#$%^&*]')

X = data[['length', 'digits', 'special']]
y = data['strength']

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, 'model.pkl')
print("Model trained and saved as model.pkl")
