import nltk
from collections import Counter

def get_features(text, setting):
    if setting=='bow':
        return {word: count for word, count in Counter(preprocess(text)).items()}
    else:
        return {word: True for word in preprocess(text)}



 all_features = [(get_features(email, 'bow'), label) for (email, label) in all_emails]

#all_features = [(get_features(email, ''), label) for (email, label) in all_emails]