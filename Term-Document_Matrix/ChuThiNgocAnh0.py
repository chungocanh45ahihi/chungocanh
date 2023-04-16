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

words = map(lambda _: re.split("\.+\"?.?\s+|,\"?\s+|\/(?!\d)|-\s+|[\s!()_\"\>:;-]+", _), open_file)

ignore_words = ['']
stem_words = map(lambda x: [stemmer.stem(w.lower()) for w in x if w not in ignore_words], words)

form_words = map(lambda x: list(map(lambda _: re.sub("[\d.,\/-]+", "Num", _),x)), stem_words)

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




print(type(doc))

# said --> d0 d1 d2 d3 d4       to --> d0 d1 d2 d3 d4         the --> d0 d1 d2 d3 d4 

# year --> d0 d1 d2 d3          for --> d0 d1 d3 d4 

# trade --> d1 d2 d4            oil --> d1 d2 d3      on --> d0 d1 d4               are --> d0 d3 d4  

# suppli --> d1 d3      product --> d0 d2          mln --> d0 d1         ago --> d2 d4        
# includ --> d1 d2      increas --> d2 d3          industri --> d1 d4    could --> d3 d4       
# bulk-1 --> d1         bill-1 --> d2       better-1 --> d3         befor-1 --> d4      blame-1 --> d0 
# basi-1 --> d1         baht-1 --> d2       becaus-1 --> d3         befor-1 --> d4 




