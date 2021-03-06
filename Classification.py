import nltk
import pickle
import os

from sklearn.naive_bayes import MultinomialNB,BernoulliNB
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords

from Utils import Utils
from DataProcessing import DataProcess


Arguments = None
Links = None
filteredWords = None


dataProcess = DataProcess.DataProcess()

class Classification(object):

    def __init__(self):
        pass

    def setWordfeatureSet(self,wordfeatures):
        global wordFeatureSet
        wordFeatureSet = wordfeatures


    def getProcessedData(self):

        processedData = dataProcess.ProcessData()
        return processedData

    def prepareTrainingData(self,Data):
        #global variables

        Arguments = dataProcess.ClassifyArguments(Data)  # holds claims premises, and major claims
        Links = dataProcess.ClassifyLinks(Data)  # holds supporting and attacking arguments
        filteredArgumentWords = dataProcess.getFilteredWords(Arguments)  # holds tagged words with claim, majorclaim, premises
        filteredLinksWords = dataProcess.getFilteredWords(Links)

        return [filteredArgumentWords,filteredLinksWords]


    def getWordFeatures(self,Data):
        # get word features from all words  yes
        word_features = dataProcess.get_word_features(dataProcess.get_words_in_doc(Data))
        return word_features


    def extract_features(self,document):
        document_words = set(document)
        features = {}
        for word in wordFeatureSet:
            features['contains(%s)' % word] = (word in document_words)
        return features



    def getTrainingSet(self,Dataset,wordFeatures):
        training_set = nltk.classify.apply_features(Dataset,wordFeatures)
        return training_set

    # Sentiment Analyzer ------------------------------------------------------------------------------------- #
    def create_word_features(self, words):
        useful_words = [word for word in words if word not in stopwords.words("english")]
        my_dict = dict([(word, True) for word in useful_words])
        return my_dict


#------------Classifiers -----------------------------------------------#

    def getNaiveBayesClassifier(self,Training_Data):

        classifier = nltk.NaiveBayesClassifier.train(Training_Data)
        self.savePickleFile(classifier,'Naivebayes.pickle')
        return classifier

    def getSklearnClassifier(self,Training_Data):

        MNB_classifier = SklearnClassifier(MultinomialNB())
        classifier = MNB_classifier.train(Training_Data)
        self.savePickleFile(classifier, 'Sklearn.pickle')
        return classifier

    def getLogisticRegressionClassifier(self,Training_Data):

        LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
        classifier = LogisticRegression_classifier.train(Training_Data)
        self.savePickleFile(classifier, 'LogisticRegression.pickle')
        return classifier

    def getBernouliSklearnClassifier(self,Training_Data):

        BNB_classifier = SklearnClassifier(BernoulliNB())
        classifier = BNB_classifier.train(Training_Data)
        self.savePickleFile(classifier, 'BernouliSklearn.pickle')
        return classifier

# ------------Classifiers -----------------------------------------------#

    def getClassifierPrediction(self,Classifier,Test_Data,wordFeature):
        self.setWordfeatureSet(wordFeature)
        return Classifier.classify(self.extract_features(Test_Data.split()))

    def getClassifierAccuracy(self,Classifier,Test_Data):
        return nltk.classify.accuracy(Classifier, Test_Data) * 100


#-------------saving pickle files--------------------#

    def savePickleFile(self,classifier,name):
        PICKLE_DIR = Utils().getPath('picklefiles')
        filename = os.path.join(PICKLE_DIR,name)
        with open(filename,'wb') as f:
            pickle.dump(classifier, f)


