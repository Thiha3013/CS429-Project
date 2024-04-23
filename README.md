# CS429 Project Report

## Abstract
This project report outlines the development, objectives, and future directions of a web scraping and indexing system. The primary goal of this project was to create an efficient and user-friendly platform for scraping web content, building an index, and providing a search interface for users. The next steps include optimizing the scraper's performance, expanding the indexing capabilities, and enhancing the user interface.

## Overview
The solution was designed to address the need for an effective way to gather, organize, and search through vast amounts of web data. The proposed system comprises a web crawler, an indexer, and a search interface, allowing users to retrieve information on books quickly and accurately.

## Design
The system's capabilities include web content scraping, real-time indexing, and query handling. User interactions with the system begin with inputting a search query, followed by the display of relevant search results. The integration of these components is designed to provide a seamless user experience, with the backend processes remaining transparent to the end-user.

## Architecture
The software components include:
- `scraper.py`:
  - Utilizes the Scrapy framework to crawl websites and collect data.
  - Creates `output.json` on run containing a list of url names and brief description of the contents
- `indexer.py`:
  - Builds an inverted index using TF-IDF weighting from the crawled documents inside `output.json`
  - Creates `index.pkl` containing generated inverted index and urls upon on run
- `processor.py`:
  - Loads `index.pkl` to copy inverted index and urls
  - Uses cosine similarity from sklearn to rank the urls with their similarity to the query
  - Handles routes towards `search.html` and `results.html`
  - Query is processed with the input from `search.html` and results are rendered in `results.html`

## Operation
Dependencies includes:
1. scrapy for crawling data necessary
2. scikit-learn for cosine similarly and inverted index generation via tf-idf
3. Flask for the creating and routing to web server

The software operates through the following commands:
1. "scrapy startproject scraper" to initialize necessary files for crawler
2. "pip install -r requirements.txt" to install necessary dependencies
3. "python scraper.py" crawl and generate data in .json format
4. "python indexer.py" utilizes json output from scraper to generate inverted index in .pkl format
5. "python processor.py" uses inverted index generated to create a web interface on port 127.0.0.1:5001 or localhost:5001, ready to present relevant urls on query

## Conclusion
The system successfully scrapes relevant urls alongside their content and indexes it for search queries. Query also returns reasonable results and the files generated were also fine. One of the possible issues that I see is due to the nature of my program rewriting the same files on the crawler run instead of starting new, it could cause corruption in data although it never occurred during my testing.

## Test Cases
<img width="624" alt="Screenshot 2024-04-22 at 7 56 56 PM" src="https://github.com/Thiha3013/CS429-Project/assets/51184715/faac862a-1bac-49b5-aefd-8bed04ad7aaf">
<img width="625" alt="Screenshot 2024-04-22 at 7 57 34 PM" src="https://github.com/Thiha3013/CS429-Project/assets/51184715/df7e0c2a-9064-473a-8880-503d30cd7a6f">
<img width="625" alt="Screenshot 2024-04-22 at 7 57 49 PM" src="https://github.com/Thiha3013/CS429-Project/assets/51184715/e5645cdf-f117-4e4e-ac36-db2ced396589">


## Source Code
The source code is documented within the Python files, with additional details in the Operation section. Dependencies are managed via requirements.txt and are open-source.

## Bibliography
- "Coding Web Crawler in Python with Scrapy". YouTube. uploaded by NeuralNine, 23 November, 2022, <https://www.youtube.com/watch?v=m_3gjHGxIJc&t=1459s>
- "Make A Python Website As Fast As Possible!". Youtube. uploaded by Tech With Tim, 13 September, 2021, <https://youtu.be/kng-mJJby8g?si=D42SkQr5WbVxOCRs>
- Chaudhary, Mukesh. "TF-IDF Vectorizer scikit-learn". 23 April, 2022, <https://medium.com/@cmukesh8688/tf-idf-vectorizer-scikit-learn-dbc0244a911a>
- DataStax. "How to Implement Cosine Similarity in Python". 30 November 2023, <https://datastax.medium.com/how-to-implement-cosine-similarity-in-python-505e8ec1d823>
