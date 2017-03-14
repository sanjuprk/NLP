import nltk
from nltk import NaiveBayesClassifier , classify

def train(features, samples_proportion):
    train_size = int(len(features) * samples_proportion)
    train_set, test_set = features[:train_size], features[train_size:]
    classifier = NaiveBayesClassifier.train(train_set)
    return train_set, test_set, classifier

train_set, test_set, classifier = train(all_features, 0.8)