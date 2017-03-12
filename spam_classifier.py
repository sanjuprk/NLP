from __future__ import print_function, division
import nltk
import os
import random
from collections import Counter
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, classify

stoplist = stopwords.words('english')   #  words like ['is','this','at'...etc] are not going to be useful during classification , these are called stopwords

#loading the data
def init_lists(folder):
    a_list = []
    file_list = os.listdir(folder)
    for a_file in file_list:
        f = open(folder + a_file, 'r')
        a_list.append(f.read())
    f.close()
    return a_list   #  a_list contains the text of every email

#preprocessing the data
def preprocess(sentence):
    lemmatizer = WordNetLemmatizer()   # lemmatization is converting strings like 'multiplying' to 'multiply'
    return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(unicode(sentence, errors='ignore')) if not word in stoplist] # lemmatize, convert to lower case, tokenize and then remove the stopwords


#extracting the features
def get_features(text, setting):
    if setting=='bow': # using bag of words as the feature, returns number of times each word appears in the email/text.
        return {word: count for word, count in Counter(preprocess(text)).items()}
    else:
        return {word: True for word in preprocess(text)}

#training using naive bayes classifier
def train(features, samples_proportion):
    train_size = int(len(features) * samples_proportion)
    # initialise the training and test sets
    train_set, test_set = features[:train_size], features[train_size:]
    #print ('Training set size = ' + str(len(train_set)) + ' emails')
    #print ('Test set size = ' + str(len(test_set)) + ' emails')
    # train the classifier
    classifier = NaiveBayesClassifier.train(train_set)
    return train_set, test_set, classifier

#testing the model on test_set
def evaluate(train_set, test_set, classifier):
    # check how the classifier performs on the training and test sets
    print ('Accuracy on the training set = ' + str(classify.accuracy(classifier, train_set)))
    print ('Accuracy of the test set = ' + str(classify.accuracy(classifier, test_set)))
    # check which words are most informative for the classifier
    classifier.show_most_informative_features(20)


if __name__ == '__main__' :
    # initialise the data
    spam = init_lists('data/spam/')
    ham = init_lists('data/ham/')
    all_emails = [(email, 'spam') for email in spam]
    all_emails += [(email, 'ham') for email in ham]
    random.shuffle(all_emails)
    #print ('Corpus size = ' + str(len(all_emails)) + ' emails')

    # extract the features
    all_features = [(get_features(email, ''), label) for (email, label) in all_emails]
    #print ('Collected ' + str(len(all_features)) + ' feature sets')

    # train the classifier
    train_set, test_set, classifier = train(all_features, 0.8)

    # evaluate its performance
    evaluate(train_set, test_set, classifier)