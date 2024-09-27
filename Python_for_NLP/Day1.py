# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 09:09:01 2024

@author: ratho
"""
import re
import spacy
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from transformers import BartTokenizer, BartForConditionalGeneration

############## Task 1 #########################
# stopwords
stop_words = set(stopwords.words('english'))

# stop words to omit
stop_words_to_omit = {'again', 'once', 'from'}

# Remove the specified stop words from the stop words list
filtered_stop_words = stop_words - stop_words_to_omit

# Print the original and filtered stop words
print("Original Stop Words:")
print(stop_words)
print("\nFiltered Stop Words:")
print(filtered_stop_words)


####################### Task 2     ############################

# NER
nlp = spacy.load("en_core_web_sm")

# NER and summarization
text = "Apple was founded by Steve Jobs in Cupertino, California. AI is revolutionizing technology."

# Named Entity Recognition (NER)
doc = nlp(text)
print("Named Entities:")
for entity in doc.ents:
    print(f"{entity.text}: {entity.label_}")

# summarization 
def summarize(text, num_sentences=1):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    word_freq = Counter(word for word in words if word not in stop_words)
    sentences = sent_tokenize(text)
    sentence_scores = {sent: sum(word_freq[word] for word in word_tokenize(sent.lower()) if word in word_freq) for sent in sentences}
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    return ' '.join(top_sentences)

summary = summarize(text, num_sentences=1)
print("Summary:", summary)

# 3. Sentiment Analysis
texts = ["I love this product", "This is bad", "I'm so happy", "This is awful"]
labels = [1, 0, 1, 0]  # 1: Positive, 0: Negative

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = LogisticRegression()
model.fit(X, labels)

new_texts = ["I feel amazing", "This is terrible"]
X_new = vectorizer.transform(new_texts)
predictions = model.predict(X_new)
print("Predictions:", predictions)
############### Task 3 ########################

# Load the model
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

# Sample text 
text = """
The United States is set to increase its presence in the Indo-Pacific region, emphasizing a commitment to defend allies and maintain stability in the face of rising tensions with China. This strategy is part of a broader defense strategy aimed at ensuring security and economic growth in the region. Officials highlighted the importance of collaboration with partners and strengthening military capabilities. The announcement comes amid concerns over China's assertive actions in the South China Sea and its growing influence in the Asia-Pacific.
"""

# Tokenize the article
inputs = tokenizer.encode("summarize: " + text, return_tensors='pt', max_length=1024, truncation=True)

# Generate summary
summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

# Print the summary
print("Original text:")
print(text)
print("\nSummary:")
print(summary)


################ Task 5 #########################
import pandas as pd
dataset=pd.read_csv("C:/8-text_mining/books.csv")