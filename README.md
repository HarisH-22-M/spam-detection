📧 Spam Email Detection App

An intelligent machine learning web app that detects whether an email or SMS text is spam or not.
Built using Python, Scikit-learn, and Streamlit, this project uses the Spambase dataset from Kaggle to train a logistic regression model capable of classifying suspicious or scam messages.

🚀 Features

🧠 Trained on the Spambase dataset from Kaggle

📊 Uses TF-IDF Vectorization to convert text into numerical features

🤖 Logistic Regression model for spam detection

🌐 Interactive Streamlit web interface for real-time predictions

💾 Model persistence using joblib for deployment

⚡ Lightweight, fast, and easily deployable on platforms like Streamlit Cloud or Render

🧩 Tech Stack

Python

Pandas, NumPy

Scikit-learn

Streamlit

Joblib

📂 Dataset

Kaggle - Spambase Dataset

🏃 How It Works

The model is trained using labeled spam and non-spam messages.

When a user pastes any email or SMS text, the app vectorizes the input using TF-IDF.

The trained model predicts whether it’s Spam (1) or Not Spam (0).

The result is displayed instantly on the Streamlit interface.

🎯 Example Inputs

Spam Example:

“Congratulations! You have won $10,000. Click the link to claim now!”

Not Spam Example:

“Hey, are we still meeting for lunch tomorrow?”
