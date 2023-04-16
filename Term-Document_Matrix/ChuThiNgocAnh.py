import os
import re
import numpy as np
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

import json


dd = "D:/IR/Term-Document_Matrix/reuters/test/"
ss = "D:/IR/Term-Document_Matrix/test/"

reuters = os.listdir(ss)
count = len(reuters)

open_file = []

for i in range(0, len(reuters)):
    f = open(ss + reuters[i], "r")
    fo = f.read()
    open_file.append(fo)

words = map(lambda _: re.split("\.+\"?.?\s+|,\"?\s+|\/(?!\d)|-\s+|[\s!()_\"\'\>:;-]+", _), open_file)

ignore_words = ['']
stop_words = set(stopwords.words('english'))
stop_words.add('')
stem_words = map(lambda x: [stemmer.stem(w.lower()) for w in x if w.lower() not in stop_words], words)

form_words = map(lambda x: list(map(lambda _: re.sub("[\d.,\/-]+", "Num", _),x)), stem_words)



print(list(stem_words))

['', 'myself', 'most', 'why', 'him', 'which', 'she', 'was', "didn't", 'do', 'into', 'in', 'aren', 
 'we', 'ma', 'your', 'down', 'as', 't', 'weren', 'were', 'themselves', 'mightn', 'what', 'own', 
 "you'll", 'y', 'by', 'same', 'theirs', 'ain', 'himself', 'i', 'under', 'don', 'her', 'mustn', 
 "couldn't", 'than', 'these', 'too', 'when', "shan't", 'each', 'and', "mightn't", "you'd", 'more', 
 "mustn't", 'through', 'doing', 'yourself', "hadn't", 'ours', 'wasn', 'those', 'won', 'be', 'yours', 
 'the', 'has', 'who', 'then', 'further', 'will', 'they', 'didn', 'or', "hasn't", 'for', 
'while', "you've", 'nor', 'you', 'between', 'shouldn', "that'll", 'on', 'out', 'both', 'other', 
'no', "don't", 've', 'haven', 'until', 'once', 
'after', 'ourselves', 'from', 'its', 'this', 'up', 'their', 'have', 'are', 'because', "needn't", 
'my', 'a', 'o', "aren't", 'only', 'again', "wasn't", "she's", 'hers', 'to', 'few', 'so', "isn't", 
"shouldn't", 'needn', 'is', 'there', "weren't", 'am', 'off', 'an', 'itself', 're', 'll', 'before', 
'where', 'it', 'very', 'above', 'how', 'been', 'against', 'd', "wouldn't", 'such', 'just', 'should', 
'had', 'doesn', 'did', 'he', 'whom', 'of', 'hadn', "haven't", 'all', 's', "should've", 'that', 'them', 
'can', 'with', "it's", 'during', 'yourselves', 'about', "doesn't", 'having', 'if', 'herself', 'but', 
'some', 'at', 'isn']