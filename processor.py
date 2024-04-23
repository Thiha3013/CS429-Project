from flask import Flask, request, jsonify, render_template, redirect, url_for
import pickle
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

def load_index(filename='index.pkl'):
    with open(filename, 'rb') as file:
        tfidf_matrix, vectorizer, urls = pickle.load(file)
    return tfidf_matrix, vectorizer, urls

tfidf_matrix, vectorizer, urls = load_index()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    try:
        shutdown_func = request.environ.get('werkzeug.server.shutdown')
        if shutdown_func is None:
            return 'Shutdown not possible: Not running the correct server.', 500
        shutdown_func()
        return 'Server shutting down', 200
    except Exception as e:
        return str(e), 500

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        top_k = int(request.form.get('top_k', 5))
        return redirect(url_for('search', query=query, top_k=top_k))
    return render_template('search.html')

@app.route('/search')
def search():
    user_query = request.args.get('query', '')
    top_k = int(request.args.get('top_k', 5))
    query_vector = vectorizer.transform([user_query])
    similarities = cosine_similarity(tfidf_matrix, query_vector).flatten()
    top_indices = similarities.argsort()[-top_k:][::-1]
    results = [{'url': urls[idx], 'score': float(similarities[idx])} for idx in top_indices]
    return render_template('./results.html', query=user_query, results=results, top_k=top_k)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
