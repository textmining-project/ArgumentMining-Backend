'''import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle


def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict


classifier_f = open("picklefiles/naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
classifier_f.close()




words = word_tokenize(review_santa)
words = create_word_features(words)
print(classifier.classify(words))
'''

