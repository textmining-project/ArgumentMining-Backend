import nltk
import Classification
import pickle

from RelationAnalyzer import RelationAnalyzer
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



# Uncomment this section in order to update the models with new training data
'''
ArgumentNaiveBayesClassifier = classification.getNaiveBayesClassifier(ArgumentTraining_set)
LinksNaiveBayesClassifier = classification.getNaiveBayesClassifier(LinksTraining_set)

ArgumentSklearnClassifier = classification.getSklearnClassifier(ArgumentTraining_set)
LinksSklearnClassifier = classification.getSklearnClassifier(LinksTraining_set)

ArgumentLogisticRegressionClassifier = classification.getLogisticRegressionClassifier(ArgumentTraining_set)
LinksLogisticRegressionClassifier = classification.getLogisticRegressionClassifier(LinksTraining_set)
'''


# essays range from 81 to 90 for test -- provide key as essay"index of essay"
test_data = dataProcess.getTestData('essay81')


# --- Loading Classifiers from pickle file ----------------#

##### Naive Bayes

Arg_naiveclassifier_f = open('picklefiles/Argument_Naivebayes.pickle', "rb")
NaiveArgumentSentimentClassifier = pickle.load(Arg_naiveclassifier_f)
Arg_naiveclassifier_f.close()

link_naiveclassifier_f = open('picklefiles/Links_Naivebayes.pickle', "rb")
NaiveLinksSentimentClassifier = pickle.load(link_naiveclassifier_f)
link_naiveclassifier_f.close()


######  Sklearn

Arg_sklearnclassifier_f = open('picklefiles/Argument_Sklearn.pickle', "rb")
SklearnArgumentSentimentClassifier = pickle.load(Arg_sklearnclassifier_f)
Arg_sklearnclassifier_f.close()

link_sklearnclassifier_f = open('picklefiles/Links_Sklearn.pickle', "rb")
SklearnLinksSentimentClassifier = pickle.load(link_sklearnclassifier_f)
link_sklearnclassifier_f.close()


###### Logistic Regression

Arg_logisticRegclassifier_f = open('picklefiles/Argument_LogisticRegression.pickle', "rb")
LogRegArgumentSentimentClassifier = pickle.load(Arg_logisticRegclassifier_f)
Arg_logisticRegclassifier_f.close()

link_logisticRegclassifier_f = open('picklefiles/Links_LogisticRegression.pickle', "rb")
LogRegLinksSentimentClassifier = pickle.load(link_logisticRegclassifier_f)
link_logisticRegclassifier_f.close()



predictedArgData = []
predictedLinkData = []


# perform claim and premise classification using classifiers
for sentence in test_data:
    NaivePrediction = classification.getClassifierPrediction(NaiveArgumentSentimentClassifier,sentence,Arg_word_features)
    predictedArg = (sentence,NaivePrediction)
    predictedArgData.append(predictedArg)
    print ("Naive Bayes prediction: ",predictedArg)

    '''
    SklearnPrediction = classification.getClassifierPrediction(SklearnArgumentSentimentClassifier, sentence,Arg_word_features)
    predictedArg = (sentence, SklearnPrediction)
    predictedArgData.append(predictedArg)
    print ("Sklearn prediction: ",predictedArg)

    LogisticRegPrediction = classification.getClassifierPrediction(LogRegArgumentSentimentClassifier, sentence,Arg_word_features)
    predictedArg = (sentence, LogisticRegPrediction)
    predictedArgData.append(predictedArg)
    print ("LogisticRegPrediction prediction: ",predictedArg)
'''



claims = []
premises = []
for item in predictedArgData:
    if item[1] == 'Premise':
        x = [item[0],item[1]]
        premises.append(x)
    if item[1] == 'Claim':
        x = [item[0],item[1]]
        claims.append(x)


#print predictedArgData

# get predicted claims and premised based on sentiment similarity score .
relationAnalyzer = RelationAnalyzer().performRelationAnalysis(claims,premises)

scoredClaimsList =  set(relationAnalyzer[0])
scoredPremiseList = relationAnalyzer[1]


# finally perform support and attacks relation classification with the scored set

for claim in scoredClaimsList:
    for premise in scoredPremiseList:
        ClaimNaivePrediction = classification.getClassifierPrediction(NaiveLinksSentimentClassifier, claim, Link_word_features)
        PremiseNaivePrediction = classification.getClassifierPrediction(NaiveLinksSentimentClassifier, premise, Link_word_features)
        if ClaimNaivePrediction == 'supports' and PremiseNaivePrediction == 'supports':
            print ('%s:Supports:%s' % (claim, premise))
        if ClaimNaivePrediction == 'attacks' and PremiseNaivePrediction == 'attacks':
            print ('%s:Attacks:%s' %(claim, premise))
        predictedLink = (sentence, NaivePrediction)
        predictedLinkData.append(predictedLink)

'''

#Get accuracy of Classifiers

accuracyTestData = dataProcess.getTestAccuracyData()
ArgumentTesting_set = accuracyTestData[0]
LinksTesting_set =  accuracyTestData[1]

#from Metrics import Metrics

#Metrics().evaluation(LinksTesting_set,NaiveArgumentSentimentClassifier)


print "Naive Bayes: ",ArgNaiveBayesScore,LinkNaiveBayesScore
print "Sklearn : ",ArgSklearnBayesScore,LinkSklearnBayesScore
print "Logistic reg: ",ArglogBayesScore,LinklogBayesScore

'''










