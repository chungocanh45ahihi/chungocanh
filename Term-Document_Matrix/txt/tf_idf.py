import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.stem.lancaster import LancasterStemmer
lancaster = LancasterStemmer()
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
import numpy as np

words = []
file = []
ignore_words = ['?', '!', '.', ',', ':','-','(',')', '>', '--', '|', '|-', "'"]
files = ['try.txt', 'catch.txt']

for item in files:
    file.append(open(item, 'r'))
    
# file = open('try.txt', 'r')
for item in file:
    words.append(item.read())

words_token=[]
for item in words:
    words_token.append(nltk.word_tokenize(item))
    

words_stem = []
for item in words_token:
    words_stem.append([stemmer.stem(w.lower()) for w in item if w not in ignore_words])

words_unique = []
for item in words_stem:
    words_unique.append(np.unique(item).tolist())

all_words = sum(words_unique, [])
all_words = np.unique(all_words).tolist() 
print(all_words)

# ============
# words = file.read()
# words = nltk.word_tokenize(words)
# print(words)
# words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
# print(stemmer.stem("car's"))
# print(words)
# # word = set(words)
# word = np.unique(words).tolist()
# print(word)






