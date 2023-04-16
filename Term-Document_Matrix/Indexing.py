import os
import re
import numpy as np
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

words = map(lambda _: re.split("[\s,.()/\-\"\'?!@#$%^&*{}<>_=+\|\:\;\\\[\]`~]", _), open_file)

ignore_words = ['']
stem_words = map(lambda x: [stemmer.stem(w.lower()) for w in x if w not in ignore_words], words)

form_words = list(map(lambda x: list(map(lambda _: re.sub("\d+", "Num", _),x)), stem_words))

for i in range(len(form_words)):
    for j in range(len(form_words[i])-1):
        bigram = '-'.join(form_words[i][j:j+2])
        form_words[i].append(bigram)

unique_words = [list(set(doc)) for doc in form_words]

flat_word = sum(unique_words, [])

all_words = np.unique(flat_word).tolist()

corpus = [("d" + str(i), doc) for i, doc in enumerate(unique_words)]
doc = {x: [p[0] for p in [(p[0], p[1].index(x)) for p in corpus if x in p[1]]] for x in all_words}
docs = map(lambda x: (x + " " + str(len(doc[x])), doc[x]), doc)

with open('index.txt', 'w') as f:
    for i in docs:
        f.write(i[0] + " ")
        for j in i[1]:
            f.write(j + " ")
        f.write('\n')
