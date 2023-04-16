from flask import Flask, render_template, request
import os
import re
import numpy as np
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
import itertools

app = Flask(__name__)
app.config['DOC'] = []

def count_words(folder_path):
    open_file = []

    for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.txt') or file.endswith(''):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        content = f.read()
                    open_file.append(content)
        
    words = (map(lambda _: re.split("[\s,.()/\-\"\'?!@#$%^&*{}<>_=+\|\:\;\\\[\]`~]", _), open_file))
    ignore_words = ['']
    stem_words = map(lambda x: [stemmer.stem(w.lower()) for w in x if w not in ignore_words], words)

    form_words = list(map(lambda x: list(map(lambda _: re.sub("\d+", "Num", _),x)), stem_words))

    for i in range(len(form_words)):
        for j in range(len(form_words[i])-1):
            bigram = ' '.join(form_words[i][j:j+2])
            form_words[i].append(bigram)

    unique_words = [list(set(doc)) for doc in form_words]

    flat_word = sum(unique_words, [])

    all_words = np.unique(flat_word).tolist()

    corpus = [("d" + str(i), doc) for i, doc in enumerate(unique_words)]
    doc = {x: [p[0] for p in [(p[0], p[1].index(x)) for p in corpus if x in p[1]]] for x in all_words}

    return (doc)

def searchId(a, id):
    return id[a]

def search_and(a,b, my_dict):
    intersection = list(set(my_dict[a]) & set(my_dict[b]))
    intersection.sort
    return intersection

def search_or(a, b, my_dict):
    union = list(set(my_dict[a]) | set(my_dict[b]))
    union.sort
    return union

def and_not(a, b, my_dict):
    andnot = list(set(my_dict[a]) - set(my_dict[b]))
    return andnot

def or_not(a, b, id):
    
    all_id = list(itertools.chain.from_iterable(id.values()))
    result = list(filter(lambda x: x not in id[b], all_id))
    result.extend(id[a])

    return list(set(result))


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/tudien', methods=['GET', 'POST'])
def tudien():
    if request.method == 'POST':
        file = request.files['file']
        folder_path = os.path.dirname(file.filename)
        app.config['DOC'] = count_words(folder_path)
        
        return render_template('tudien.html', file_count=app.config['DOC'])
    return render_template('tudien.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        doc = app.config['DOC']

        search_type = request.form['searchType']
        search_results = []

        if search_type == 'search':
            query = request.form['searchText']
            search_results = searchId(query, doc)

        elif search_type == 'searchAnd':
            query1 = request.form['searchText']
            query2 = request.form['searchText2']
            search_results = search_and(query1, query2, doc)

        elif search_type == 'searchOr':
            query1 = request.form['searchText']
            query2 = request.form['searchText2']
            search_results = search_or(query1, query2, doc)
        
        elif search_type == 'andNot':
            query1 = request.form['searchText']
            query2 = request.form['searchText2']
            search_results = and_not(query1, query2, doc)
        
        elif search_type == 'orNot':
            query1 = request.form['searchText']
            query2 = request.form['searchText2']
            search_results = or_not(query1, query2, doc)

        return render_template('search.html', file_count=doc, search_results=search_results)

    return render_template('search.html')



if __name__ == '__main__':
    app.run(debug=True)
