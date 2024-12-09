import requests
from bs4 import BeautifulSoup
import spacy
from heapq import nlargest
from string import punctuation
import json
from bs4 import BeautifulSoup
import re

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Function to calculate word frequencies
def word_frequency(doc):
    stopwords = spacy.lang.en.stop_words.STOP_WORDS
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
    return word_frequencies


# Function to calculate sentence scores
def sentence_score(sentence_tokens, word_frequencies):
    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
    return sentence_scores

# Function to summarize text
def get_summary(text):
    doc = nlp(text)
    word_frequencies = word_frequency(doc)
    max_freq = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] /= max_freq
    sentence_tokens = [sent for sent in doc.sents]
    sentence_scores = sentence_score(sentence_tokens, word_frequencies)
    select_length = int(len(sentence_tokens) * 0.1)
    summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
    summary = [sent.text for sent in summary]
    return " ".join(summary)

# Function to fetch news links and details
def fetch_news_links(query):
    news_api_key = "5890574551aa4c23b6b3511ca8bbf734"  # Replace with your NewsAPI key
    req_url = f"https://newsapi.org/v2/everything?sources=bbc-news&q={query}&language=en&apiKey={news_api_key}"
    response = requests.get(req_url).json()
    link_list, title_list, thumbnail_list = [], [], []
    for article in response.get("articles", []):
        link_list.append(article["url"])
        title_list.append(article["title"])
        thumbnail_list.append(article.get("urlToImage", ""))
    return link_list, title_list, thumbnail_list

# Function to fetch news content
def fetch_news(link_list):
    news_list = []
    for link in link_list:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.findAll("p")
        article_text = " ".join([para.get_text() for para in paragraphs])
        news_list.append(article_text)
    return news_list

# Function to tokenize text using spaCy
def spacy_tokenizer(text):
    doc = nlp(text)
    return [token.text for token in doc]

# Simple custom tokenizer (expected tokenization) for comparison
def custom_tokenizer(text):
    # Use a regular expression to split text into words and punctuation
    return re.findall(r'\w+|[^\w\s]', text)

# Function to evaluate tokenization quality
def evaluate_tokenizer_quality(nlp, user_text):
    # Tokenize using spaCy
    predicted_tokens = spacy_tokenizer(user_text)
    
    # Generate expected tokens using the custom tokenizer
    expected_tokens = custom_tokenizer(user_text)
    
    # Calculate precision, recall, and F1-score
    correct_tokens = set(predicted_tokens) & set(expected_tokens)
    precision = len(correct_tokens) / len(predicted_tokens) if predicted_tokens else 0
    recall = len(correct_tokens) / len(expected_tokens) if expected_tokens else 0
    f1_score = (
        2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    )
    
    return {
        "Predicted Tokens": predicted_tokens,
        "Expected Tokens": expected_tokens,
        "Precision": precision * 100,
        "Recall": recall * 100,
        "F1-Score": f1_score * 100,
    }
# Function to calculate ROUGE scores
def calculate_rouge(reference, hypothesis):
    """
    Calculate ROUGE scores between a reference and hypothesis text.
    Args:
        reference (str): The reference summary text.
        hypothesis (str): The generated summary text.
    Returns:
        dict: ROUGE-1, ROUGE-2, and ROUGE-L scores (Precision, Recall, F1).
    """
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference, hypothesis)
    return {
        "ROUGE-1": scores["rouge1"],
        "ROUGE-2": scores["rouge2"],
        "ROUGE-L": scores["rougeL"]
    }
