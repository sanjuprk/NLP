
 ## Sentence Classification:
 
 A good example of classifying sentences is Sentiment analysis. We perform this on the data movie_reviews imported from
 nltk.corpus
 
 #### STEPS:
* Importing data
* Extracting features from the names data
* Training using NaiveBayes 
* Classifying new data using NaiveBayes

The features we used are:
* Bag of Words (counting)i.e how many times the word occurs in the sentence is also considered.
* Bag of words (existance) i.e only checks if the word is present or not in the sentence.

Both these features work well classifying the documents but not so well with sentences because with documents there are large number of words whereas with sentences it is like predicting with very little data.
