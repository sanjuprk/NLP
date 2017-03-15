 
 ## Part Of Speech TAGGER:
 
 Objective: Tagging every word in a large amount of text with its corresponding parts of speech.
 
 The `Brown` dataset on which we assign the POS is imported from the nltk corpora/`nltk.corpus`. 
 
  We use many POS Taggers from the `nltk` library. Some of them are :
  * Default Tagger
  * Unigram Tagger 
  * RegExp Tagger
  * Affix Tagger
  * Ngram Tagger
 
 ### Default Tagger:
 It assigns a default value to all the words. Accuracy is obviously very low. But can be used as a good backoff tagger. Since assigns a default value doesn't require any training.
 
 ### Unigram Tagger:
 Also known as lookup tagger. While learning from the training set it establishes a dictionary which it can look up while classifying the test set. In the dictionary the frequency with which a particular word is assigned a particular POS is also stored. This along with Default Tagger as a backoff gives fairly good accuracy.
 
 ### RegExp Tagger:
 This depends on morphology of the word i.e the starting or ending letters, eg. a non-verb ending with 'ly' is usually an adverb.Fairly low accuracy though. The Morphology to be checked is given by the programmer.
 
 ### Affix Tagger:
 Similar to RegExp Tagger , tries to find patterns among the words.Learns rules from the last letters(usually last 3 *xyz).
 ### Ngram Tagger:
 Also called context tagger since the learning is based on not just that word but the n preceding words.
 
 
 If all of these taggers are used as backoff to each other, then the accuracy of tagging is the highest.
 