# HEJ Front-end!!
# Ropa på get_random_words för en lista på 50 ord skapad av en människa
# Ropa på get_occupation2 och skicka in upp till 5 ord och få tillbaka en lista på 5 yrken
# 3-5 ord fungerar bäst. Om ni skickar färre än 5, skicka med tomma strängar för resterande ord t.ex 
# Get_occupation('hjälpsam', 'noggrann', 'ledning', '', '')
# Ni får snabbt tillbaka en lista på 5 occupations som passar
# Varma hälsningar


import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# Skickar ord att fylla bubblorna med till frontend.
# Hämtar från fil

def new_get_random_words():
    with open(('ord_till_frontend.txt'), 'r') as file:
        words = file.read().splitlines()
    
    if 50 >= len(words):
        return words
    
    random_words = random.sample(words, 50)
    return random_words

def get_random_words():
    words = new_get_random_words()
    return words


## Gets 15 egenskaper

def get_egenskaper():
    with open(('ord_egenskaper.txt'), 'r') as file:
        words = file.read().splitlines()
    
    if 15 >= len(words):
        return words
    
    random_words = random.sample(words, 15)

    return random_words

# Gets 15 arbetsuppgifter

def get_arbetsuppgifter():
    with open(('ord_arbetsuppgifter.txt'), 'r') as file:
        words = file.read().splitlines()
    
    if 15 >= len(words):
        return words
    
    random_words = random.sample(words, 15)

    return random_words

## Takes x amount of words, returns 5 suitable occupations using cosine similarity. Used by frontend. 

def get_occupation2(word1, word2, word3, word4, word5):
    # Load occupation data
    print('Reading dataset...')
    df = pd.read_csv('dataset2022.csv')
    print('dataset read!')

    # Preprocess occupation descriptions. Puts words into vectors for each  
    print('Processing occupation descriptions...')
    tfidf = TfidfVectorizer()
    description_vectors = tfidf.fit_transform(df['description'].fillna(''))

    # Create input vector by transforming a string containing three words (word1, word2, and word3) 
    # using the same TfidfVectorizer instance. The resulting vector is stored in a variable called "input_vector".
    print('Creating input vector...')

    input_vector = tfidf.transform([' '.join([word1, word2, word3, word4, word5])])
    print('Input vector created')

    # Compute cosine similarity (similarity between two vectors) between input vector and occupation description vectors
    print('Matching...')
    similarity_scores = cosine_similarity(input_vector, description_vectors)


    # Rank occupations by similarity score and return top 5
    top_occupations = np.argsort(similarity_scores, axis=1)[:, -5:].squeeze()[::-1]
    return df.iloc[top_occupations]['occupation'].tolist()


#print(get_occupation2('säkerhet', 'människor', 'social', 'utåtriktad', 'vakt'))


