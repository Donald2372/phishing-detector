import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from preprocessing import clean_text, vectorize_text
import joblib

# Chargement du dataset
df = pd.read_csv('data/emails.csv')

# Renommer les colonnes pour simplifier
df = df.rename(columns={'Email Text': 'text', 'Email Type': 'label'})

# Supprimer les lignes avec texte manquant
df = df.dropna(subset=['text'])

# Nettoyage du texte
df['clean_text'] = df['text'].apply(str).apply(clean_text)

# Vectorisation
X, vectorizer = vectorize_text(df['clean_text'])

# Transformation des étiquettes
df['label'] = df['label'].map({'Safe Email': 0, 'Phishing Email': 1})
y = df['label']

# Split des données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement du modèle
model = MultinomialNB()
model.fit(X_train, y_train)

# Évaluation
print(classification_report(y_test, model.predict(X_test)))

# Sauvegarde
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
