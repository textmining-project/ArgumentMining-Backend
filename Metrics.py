
import collections
import nltk
from nltk import precision, recall, f_measure


class Metrics(object):

    def __init__(self):
        pass

    def evaluation(self,test_set, classifier):
        referenceSet = collections.defaultdict(set)
        testSet = collections.defaultdict(set)
        referenceSet_cm = []
        testSet_cm = []

        for index, (sentences, actualLabel) in enumerate(test_set):
            referenceSet[actualLabel].add(index)
            referenceSet_cm.append(actualLabel)
            predictedLabel = classifier.classify(sentences)
            testSet[predictedLabel].add(index)
            testSet_cm.append(predictedLabel)

        print referenceSet.keys()
        print testSet.keys()



        print ("-------------Claim metrics-----------")
        print ('Accuracy of the classifier:  ', nltk.classify.util.accuracy(classifier, test_set))
        print ('precision:           ', precision(referenceSet[referenceSet.keys()[0]], testSet[testSet.keys()[0]]))
        print ('recall:              ', recall(referenceSet[referenceSet.keys()[0]], testSet[testSet.keys()[0]]))
        print ('F-measure:           ', f_measure(referenceSet[referenceSet.keys()[0]], testSet[testSet.keys()[0]]))

        print ("-------------Premise metrics-----------")
        print ('Accuracy of the classifier:  ', nltk.classify.util.accuracy(classifier, test_set))
        print ('precision:           ', precision(referenceSet[referenceSet.keys()[1]], testSet[testSet.keys()[1]]))
        print ('recall:              ', recall(referenceSet[referenceSet.keys()[1]], testSet[testSet.keys()[1]]))
        print ('F-measure:           ', f_measure(referenceSet[referenceSet.keys()[1]], testSet[testSet.keys()[1]]))


