# Tạo bộ từ vựng
import string

def create_vocabulary(documents):
    vocabulary = set()
    for doc in documents:
        words = doc.lower().translate(str.maketrans('', '', string.punctuation)).split()
        vocabulary.update(words)
    return vocabulary

# Tạo bộ chỉ mục và tính toán IDF
import math

def create_index(documents):
    index = {}
    n = len(documents)
    vocabulary = create_vocabulary(documents)
    for term in vocabulary:
        df = sum(1 for doc in documents if term in doc.lower())
        idf = math.log(n / df)
        index[term] = idf
    return index

# Tài liệu
d1 = "Tom loves Jerry."
d2 = "Jerry likes a dog, not Tom."
d3 = "The dog liked 10 cats."

# Lập chỉ mục
documents = [d1, d2, d3]
index = create_index(documents)

# Tạo hàm tính vector TF-IDF
def compute_tfidf_vector(doc, index):
    tfidf = {}
    words = doc.lower().translate(str.maketrans('', '', string.punctuation)).split()
    word_counts = {word: words.count(word) for word in words}
    doc_length = len(words)
    for word in words:
        if word in index:
            tf = word_counts[word] / doc_length
            idf = index[word]
            tfidf[word] = tf * idf

    return tfidf

# Tính toán vector TF-IDF của các tài liệu
tfidf_docs = []
for doc in documents:
    tfidf_docs.append(compute_tfidf_vector(doc, index))

print(tfidf_docs)


# Tính toán vector TF-IDF của truy vấn
query = "Tom loves Jerry"
tfidf_query = compute_tfidf_vector(query, index)

# Tạo hàm tính độ đo cosine
def cosine_similarity(vec1, vec2):
    common_terms = set(vec1.keys()) & set(vec2.keys())
    dot_product = sum(vec1[term] * vec2[term] for term in common_terms)
    magnitude1 = math.sqrt(sum(val**2 for val in vec1.values()))
    magnitude2 = math.sqrt(sum(val**2 for val in vec2.values()))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    else:
        return dot_product / (magnitude1 * magnitude2)

# Tính toán điểm tương đồng giữa truy vấn và các tài liệu
scores = []
for doc in tfidf_docs:
    score = cosine_similarity(doc, tfidf_query)
    scores.append(score)

print("-------------------------------------")
# Sắp xếp và trình bày kết quả cho người dùng
results = sorted(zip(scores, documents), reverse=True)
for score, doc in results:
    print(f"Score: {score:.3f} - Document: {doc}")
