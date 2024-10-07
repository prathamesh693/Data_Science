# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 09:01:45 2024

@author: ratho
"""
# extract in python 
''' phone no, title, dates, and design a patterns
'''
sentence5="The cute little boy is playing 100 of kitten"
from nltk import ngrams
# extraction n-grams with nltk
list(ngrams("The cute little boy is playing 100 of kitten".split(),2))
list(ngrams("The cute little boy is playing with kitten".split(),3))

from textblob import TextBlob
blob=TextBlob("The cute little boy is playing with kitten.")
blob.ngrams(n=2)

sentence5
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence5)

#################################
# tokenixation using TextBlob
from textblob import TextBlob
blob=TextBlob(sentence5)
blob.words
#######
from nltk.tokenize import TweetTokenizer
tweet_tikenizer=TweetTokenizer()
tweet_tikenizer.tokenize(sentence5)
## multi word expression 
from nltk.tokenize import MWETokenizer
''' 
multi word tokenizers are essential fro tasks 
where the meaning of the text heavily depedst on the 
interpretation of pharases as wholes rather than as 
sums of individual words. for instance,
in sentiment analysis, recognizing  "not good" 
as a single negative sentiment unit rather than as
"not" and "good" separately can significantly affect 
the outcome.
'''

sentence5
mwe_tokenizer=MWETokenizer([('of','kitten')])
mwe_tokenizer.tokenize(sentence5.split())
mwe_tokenizer.tokenize(sentence5.replace('100'," ").split())

### parse matrix












