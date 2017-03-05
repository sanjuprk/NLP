import nltk
from nltk import word_tokenize, WordNetLemmtizer
from nltk.corpus import stopwords

stoplist = stopwords.words('english')
lemmatizer = WordNetLemmtizer()


# in preprocessing we convert the sentence to tokens, tokens/words to lower case and then lemmatize the tokens

def preprocess(sentence):
    return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(sentence) if not word in sentence]

    