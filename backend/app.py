from flask import Flask, request, jsonify
import joblib
import re

app = Flask(__name__)
model = joblib.load('model.pkl')

def extract_features(password):
    length = len(password)
    digits = len(re.findall(r'\d', password))
    special = len(re.findall(r'[!@#$%^&*]', password))
    return [[length, digits, special]]

@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.json
    password = data.get('password', '')
    features = extract_features(password)
    strength = model.predict(features)[0]
    strength_map = {0: 'weak', 1: 'medium', 2: 'strong'}
    return jsonify({'strength': strength_map[strength]})

if __name__ == '__main__':
    app.run(debug=True)
