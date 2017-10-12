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

from RelationAnalyzer import RelationAnalyzer
from DictionaryTagger import DictionaryTagger
from bratreader.repomodel import RepoModel
from nltk.tokenize import word_tokenize
from DataProcessing import DataProcess

dataProcess = DataProcess.DataProcess()

classification = Classification.Classification()

# Get Raw data in Processed
processedData = classification.getProcessedData()

# prepare Training data from raw data
preTrainingData = classification.prepareTrainingData(processedData) #arguments and links
Arguments = preTrainingData[0]
Links = preTrainingData[1]


#get word features from training data
Arg_word_features = classification.getWordFeatures(Arguments)
Link_word_features = classification.getWordFeatures(Links)


def Arg_Extract_features(document):
    document_words = set(document)
    features = {}
    for word in Arg_word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features


def Link_Extract_features(document):
    document_words = set(document)
    features = {}
    for word in Link_word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features



ArgumentTraining_set = nltk.classify.apply_features(Arg_Extract_features, Arguments)
LinksTraining_set = nltk.classify.apply_features(Link_Extract_features, Links)

'''
# Uncomment this section in order to update the models with new training data

ArgumentNaiveBayesClassifier = classification.getNaiveBayesClassifier(ArgumentTraining_set)
LinksNaiveBayesClassifier = classification.getNaiveBayesClassifier(LinksTraining_set)

ArgumentSklearnClassifier = classification.getSklearnClassifier(ArgumentTraining_set)
LinksSklearnClassifier = classification.getSklearnClassifier(LinksTraining_set)

ArgumentLogisticRegressionClassifier = classification.getLogisticRegressionClassifier(ArgumentTraining_set)
LinksLogisticRegressionClassifier = classification.getLogisticRegressionClassifier(LinksTraining_set)
 
'''



# essays range from 81 to 90 for test -- provide key as essay"index of essay"
test_data = dataProcess.getTestData('essay81')


print test_data


Arg_naiveclassifier_f = open('picklefiles/Argument_Naivebayes.pickle', "rb")
ArgumentSentimentClassifier = pickle.load(Arg_naiveclassifier_f)
Arg_naiveclassifier_f.close()


link_naiveclassifier_f = open('picklefiles/Links_Naivebayes.pickle', "rb")
LinksSentimentClassifier = pickle.load(link_naiveclassifier_f)
link_naiveclassifier_f.close()

predictedArgData = []
predictedLinkData = []


# perform claim and premise classification
for sentence in test_data:
    NaivePrediction = classification.getClassifierPrediction(ArgumentSentimentClassifier,sentence,Arg_word_features)
    predictedArg = (sentence,NaivePrediction)
    predictedArgData.append(predictedArg)
    #print predictedData
    #print("Argument Naive Bayes : %s -- %s  " % (sentence,NaivePrediction))




claims = []
premises = []
for item in predictedArgData:
    if item[1] == 'Premise':
        x = [item[0],item[1]]
        premises.append(x)
    if item[1] == 'Claim':
        x = [item[0],item[1]]
        claims.append(x)



# get predicted claims and premised based on sentiment similarity score .
relationAnalyzer = RelationAnalyzer().performRelationAnalysis(claims,premises)

scoredClaimsList =  set(relationAnalyzer[0])
scoredPremiseList = relationAnalyzer[1]


# finally perform support and attacks relation classification with the scored set
print "RELATION -------------------------"
for claim in scoredClaimsList:
    for premise in scoredPremiseList:
        ClaimNaivePrediction = classification.getClassifierPrediction(LinksSentimentClassifier, claim, Link_word_features)
        PremiseNaivePrediction = classification.getClassifierPrediction(LinksSentimentClassifier, premise, Link_word_features)
        if ClaimNaivePrediction == 'supports' and PremiseNaivePrediction == 'supports':
            print ("Claim:%s","Supports","Premise:%s",claim,premise)
        #predictedLink = (sentence, NaivePrediction)
        #predictedLinkData.append(predictedLink)
        # print predictedData
        # print("Link Naive Bayes : %s -- %s  " % (sentence,NaivePrediction))















