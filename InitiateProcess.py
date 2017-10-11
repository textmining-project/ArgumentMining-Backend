import classifier as classifier
import nltk
import bratreader
import Splitter
import POSTagger
import DataProcessing
import time
import Classification
import DataProcessing
import pickle
import os

from DictionaryTagger import DictionaryTagger
from bratreader.repomodel import RepoModel
from nltk.tokenize import word_tokenize
from DataProcessing import DataProcess

dataProcess = DataProcess.DataProcess()

classification = Classification.Classification()

# Get Raw data in Processed
processedData = classification.getProcessedData()

# prepare Training data from raw data
primaryTrainingData = classification.prepareTrainingData(processedData) #arguments

#get word features from training data
word_features = classification.getWordFeatures(primaryTrainingData)


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


training_set = nltk.classify.apply_features(extract_features, primaryTrainingData)


NaiveBayesClassifier = classification.getNaiveBayesClassifier(training_set)
LogisticRegClassifier = classification.getLogisticRegressionClassifier(training_set)


# essays range from 81 to 90 for test -- provide key as essay"index of essay"
test_data = dataProcess.getTestData('essay81')
print test_data


naiveclassifier_f = open('picklefiles/naivebayes.pickle', "rb")
SentimentClassifier = pickle.load(naiveclassifier_f)
naiveclassifier_f.close()



predictedData = []
for sentence in test_data:
    NaivePrediction = classification.getClassifierPrediction(NaiveBayesClassifier,sentence,word_features)
    predicted = (sentence,NaivePrediction)
    predictedData.append(predicted)
    #print predictedData
    #print("Naive Bayes : %s -- %s  " % (sentence,NaivePrediction))


# After claim and premise predition - Finding relations between claim and premise

SentimentClassifiedData = []
for item in predictedData:
    testString = item[0]
    words = word_tokenize(testString)
    words = classification.create_word_features(words)
    sentiment = SentimentClassifier.classify(words)
    x = list(item)
    x.append(sentiment)
    SentimentClassifiedData.append(tuple(x))

print SentimentClassifiedData


















