import joblib
from preprocessing import clean_text

model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

def predict(text):
    clean = clean_text(text)
    vector = vectorizer.transform([clean])
    pred = model.predict(vector)[0]
    return "Phishing" if pred == 1 else "Safe"

# Exécution simple
email = input("Entrez votre e-mail :\n")
print(predict(email))
