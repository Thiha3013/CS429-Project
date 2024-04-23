import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_documents(file_path='output.json'):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return [(doc['content'], doc['url']) for doc in data]

def build_index(documents):
    vectorizer = TfidfVectorizer(
        stop_words='english',
        min_df=2,
        max_df=0.5,
        ngram_range=(1, 2)
    )
    contents = [doc[0] for doc in documents]
    urls = [doc[1] for doc in documents]
    tfidf_matrix = vectorizer.fit_transform(contents)
    return tfidf_matrix, vectorizer, urls

def save_index(tfidf_matrix, vectorizer, urls, filename='index.pkl'):
    with open(filename, 'wb') as file:
        pickle.dump((tfidf_matrix, vectorizer, urls), file)

def load_index(filename='index.pkl'):
    with open(filename, 'rb') as file:
        tfidf_matrix, vectorizer, urls = pickle.load(file)
    return tfidf_matrix, vectorizer, urls


def calculate_cosine_similarity(tfidf_matrix, query_vector):
    return cosine_similarity(tfidf_matrix, query_vector)


# usage
if __name__ == "__main__":
    documents = load_documents() 
    tfidf_matrix, vectorizer, urls = build_index(documents)  
    save_index(tfidf_matrix, vectorizer, urls) 

    
