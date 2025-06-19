import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'\W', ' ', text)    # Remove non-word characters
    text = text.lower()
    text = ' '.join(word for word in text.split() if word not in stop_words)
    return text

def vectorize_text(corpus):
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(corpus)
    return X, vectorizer

if __name__ == "__main__":
    print(clean_text("This is a <b>test</b> message!"))
