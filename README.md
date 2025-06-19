# 📧 Email Phishing Detector

A machine learning project that detects whether an email is a legitimate message or a phishing attempt, using Natural Language Processing (NLP) techniques and logistic regression.

---

## 🚀 Project Overview

Phishing is one of the most common forms of cyber attacks. This project uses machine learning to analyze the content of emails and classify them as either:

- ✅ **Safe Email**  
- ⚠️ **Phishing Email**

The model has been trained on a labeled dataset of real and synthetic emails, and it achieves over 94% accuracy with a balanced tolerance between false positives and false negatives.

---

## 🧠 Technologies Used

- Python 3.11+
- scikit-learn
- pandas
- Flask (for the backend API)
- HTML/CSS/JavaScript (for the frontend)
- TfidfVectorizer (for NLP text vectorization)
- LogisticRegression (as the classifier)

---

## 📂 Project Structure

```
phishing-detector/
├── data/
│   └── emails.csv                # Labeled dataset (text, label)
├── preprocessing.py              # Text cleaning functions
├── model.py                      # Trains and saves the model
├── model_pipeline.pkl            # Trained pipeline (TF-IDF + model)
├── server.py                     # Flask API backend
├── index.html                    # Web interface (frontend)
└── README.md                     # Project documentation
```

---

## 🧪 How It Works

1. **Preprocessing:**  
   Emails are cleaned and converted into TF-IDF vectors.

2. **Training:**  
   A logistic regression model is trained on labeled email data.

3. **Inference:**  
   New email content is passed to the trained model through a web form. The server responds with a classification and a confidence score.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/phishing-detector.git
cd phishing-detector
```

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate        # On Windows
source .venv/bin/activate    # On Linux/macOS
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

(If you don’t have a `requirements.txt`, install manually:)

```bash
pip install flask flask-cors pandas scikit-learn
```

### 4. Run the Backend Server

```bash
python server.py
```

You should see:  
`Running on http://127.0.0.1:5000`

---

## 🌐 Using the Web Interface

To interact via the browser:

```bash
python -m http.server 8000
```

Then open in your browser:

```
http://localhost:8000/index.html
```

Paste your email content, click **Analyze**, and view the prediction.

---

## 📈 Model Performance

- Accuracy: ~94%
- Precision: 0.91 (Safe), 0.99 (Phishing)
- False Positive Rate: Reduced with a custom threshold of 0.7

---

## ✅ Examples

### Safe Email

```
Hello Donald, your Amazon package has been shipped. You can track it here: https://amazon.fr/track...
```

### Phishing Email

```
Dear user, your PayPal account has been suspended. Click here immediately to restore access: http://paypl-login-fraud.com
```

---

## 📌 Future Improvements

- Train on larger and multilingual datasets
- Deploy via Docker or cloud service (Heroku, GCP)
- Add advanced NLP techniques (BERT, LSTM)
- Add spam explanation (highlight suspicious parts)

---

## 📬 Credits

Developed by SADJOU ELVIS DONALD   Project – NLP & Cybersecurity  
TU Clausthal – 2025

---

## 📄 License

MIT License – Feel free to use and modify.
