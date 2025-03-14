import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix
import numpy as np
import itertools
import matplotlib.pyplot as plt

st.title("Sentiment Analyzer Based On Text Analysis ")
st.write('\n\n')

@st.cache_data
def get_all_data():
    root = "Datasets/"
    with open(root + "imdb_labelled.txt", "r") as text_file:
        data = text_file.read().split('\n')
         
    with open(root + "amazon_cells_labelled.txt", "r") as text_file:
        data += text_file.read().split('\n')

    with open(root + "yelp_labelled.txt", "r") as text_file:
        data += text_file.read().split('\n')

    return data

all_data = get_all_data()

if st.checkbox('Show Dataset'):
    st.write(all_data)

@st.cache_data
def preprocessing_data(data):
    processing_data = []
    for single_data in data:
        if len(single_data.split("\t")) == 2 and single_data.split("\t")[1] != "":
            processing_data.append(single_data.split("\t"))

    return processing_data

if st.checkbox('Show PreProcessed Dataset'):
    st.write(preprocessing_data(all_data))

@st.cache_data
def split_data(data):
    total = len(data)
    training_ratio = 0.75
    training_data= []
    evaluation_data = []

    for indice in range(total):
        if indice < total * training_ratio:
            training_data.append(data[indice])
        else:
            evaluation_data.append(data[indice])

    return training_data, evaluation_data

@st.cache_data
def preprocessing_step():
    data = get_all_data()
    processing_data = preprocessing_data(data)
    return split_data(processing_data)

@st.cache_resource
def training_step(_data):
    vectorizer = CountVectorizer(binary=True)  # Initialize vectorizer inside the function
    training_text = [_data[0] for _data in _data]
    training_result = [_data[1] for _data in _data]
    training_text = vectorizer.fit_transform(training_text)
    model = BernoulliNB().fit(training_text, training_result)
    return model, vectorizer  # Return both classifier and fitted vectorizer

training_data, evaluation_data = preprocessing_step()
classifier, vectorizer = training_step(training_data)  # Get trained classifier & fitted vectorizer

def analyse_text(classifier, vectorizer, text):
    if not hasattr(vectorizer, "vocabulary_"):
        st.error("Error: Vectorizer is not fitted. Train the model first.")
        return text, None
    return text, classifier.predict(vectorizer.transform([text]))

def print_result(result):
    text, analysis_result = result
    if analysis_result is None:
        return text, "Error: Unable to analyze"
    print_text = "Positive" if analysis_result[0] == '1' else "Negative"
    return text, print_text

review = st.text_input("Enter The Review", "Write Here...")
if st.button('Predict Sentiment'):
    result = print_result(analyse_text(classifier, vectorizer, review))
    st.success(result[1])
else:
    st.write("Press the above button..")
