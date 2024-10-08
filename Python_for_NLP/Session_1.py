# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 09:00:04 2024

@author: ratho
"""
###################################Text Mining ##############################
sentence ="we are learning TextMining From Sanjivani AI"
# if we want to know the position of learning 
sentence.index("learning")
# It will show learning posotion which is 7 
sentence.split().index("TextMining")
# it will show you the position of word  at which position the word is
sentence.split()[2][::-1]
# it will to tokanation and at 2 position the string eill be get reverse 
#learning will be print reverse gninrael

#suppose want to print first and last word of the sentence 
word=sentence.split() #tokanization
first_word=word[0]
first_word
last_word=word[-1]
last_word 
##concate the first and last word
concat_word=first_word+""+last_word
concat_word

#print even words from the sentence 
[word[i] for i in range (len(word)) if i%2==0]
#words having odd length 

sentence 
sentence[-3::] # here in output there will be space in start as -3 locates has a space 
sentence[-2::]

sentence[::-1]
#All the sentence will be showing in the reverse order 

word
print(" ".join(word[::-1] for word in word))
#it is the dot join method 
#############################################
#tokenization 
import nltk 
nltk.download('punkt')
from nltk import word_tokenize
word=word_tokenize("I am reading NLP fundamentals")
print(word)
#################

#parts of speech tagging

nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(word)
"""
[('I', 'PRP'),
 ('am', 'VBP'),
 ('reading', 'VBG'),
 ('NLP', 'NNP'),
 ('Fundamentals', 'NNS')]"""

#stop words from nltk 
from nltk.corpus import stopwords

import nltk
nltk.download('stopwords')
stop_words =stopwords.words('English')
print(stop_words)