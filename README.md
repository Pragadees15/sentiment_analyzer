# Sentiment Analyzer Based On Text Analysis

## Overview
This is a **Sentiment Analyzer** built using **Streamlit** and **Naive Bayes** classification. It analyzes textual reviews and predicts their sentiment as either **Positive** or **Negative**.

## Features
- Loads labeled review datasets from IMDb, Amazon, and Yelp.
- Preprocesses the dataset by splitting it into training and evaluation sets.
- Uses **Bernoulli Naive Bayes** for sentiment classification.
- Provides a **Streamlit UI** for user interaction.
- Allows users to enter custom text for sentiment prediction.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**
   ```sh
   git clone https://github.com/Pragadees15/sentiment-analyzer.git
   cd sentiment-analyzer
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

## Requirement
- Scikit-Learn
- Python 3
- Streamlit
- Numpy
- Matplotlib

## Running the Application

To start the Streamlit app, run:
```sh
streamlit run app.py
```

## Dataset Used
The project uses labeled sentiment datasets from:
- IMDb
- Amazon
- Yelp

These datasets are stored in the `Datasets/` folder.

## How It Works
1. The datasets are loaded and preprocessed.
2. The data is split into training (75%) and evaluation (25%) sets.
3. A **CountVectorizer** is used to convert text into feature vectors.
4. A **Bernoulli Naive Bayes classifier** is trained on the vectorized data.
5. The model is used to analyze user-inputted text and predict sentiment.
6. The sentiment prediction is displayed in the Streamlit UI.

## UI Features
- Checkbox to view raw dataset and preprocessed dataset.
- Input box for users to enter custom text.
- **"Predict Sentiment"** button to analyze user input.
- Output showing whether the sentiment is **Positive** or **Negative**.

## Technologies Used
- **Python**
- **Streamlit**
- **Scikit-learn**
- **NumPy**
- **Matplotlib**


