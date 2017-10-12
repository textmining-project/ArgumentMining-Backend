import nltk
import os
from bratreader.repomodel import RepoModel
from Utils import Utils

bratessayFolder = Utils().getPathToFile('bratessays')

reader = RepoModel(bratessayFolder)

#doc = reader.documents["essay01"]		# get document with key 001
#print("sentences",doc.sentences)    			# a list of sentences in document
#print("annotation :",doc.annotations)       # the annotation objects in a documennt

completeset = []

class DataProcess(object):

    reader = RepoModel(bratessayFolder)  # load repomodel

    def __init__(self):
        pass

    def ProcessData(self):
        for i in range(1, 91):
            doc = reader.documents["essay" + str(i)]
            dataObjectList = []
            annotatedData = set(doc.annotations)
            for annotation in annotatedData:
                # print("annotation :", annotation.repr)
                # print("labels :", annotation.labels.items())
                # print("links :", annotation.links)
                # print("********************************************************************************")

                dataObject = {"annotation": annotation.repr,
                              "labels": annotation.labels.items(),
                              "links": annotation.links}

                dataObjectList.append(dataObject)

            data = self.ExtractDataFeatures(dataObjectList, doc.key)

        return data



    def ExtractDataFeatures(self,data,key):

        full = {}
        wholeobject = []
        labs = []
        links = []
        for items in data:
            sentence = items['annotation']
            full['sentence'] = sentence
            for label in items['labels']:
                for lab in label:
                    if lab != None and lab != []:
                        labs.append(lab)
            full['label'] = labs
            labs = []
            for link in items['links'].iteritems():
               lnk = link[0]
               for x in link[1]:
                   linkk = {lnk:x.repr}
                   links.append(linkk)
               full['links'] = links
               links = []

            wholeobject.append(full)
            full = {}

        completeset.append({key:wholeobject})
        return completeset



    def ClassifyArguments(self,dataset):
        ArgumentComponent = []
        for essay in dataset:
            for item in essay.values():
                for x in item:
                    for label in x['label']:
                        if label == 'Claim' or label == 'MajorClaim' or label == 'Premise':
                            filteredObj = (label, x['sentence'])
                            ArgumentComponent.append(filteredObj)


        return ArgumentComponent



    def ClassifyLinks(self,data):
        Links = []
        for essay in data:
            for item in essay.values():
                for x in item:
                    for link in x:
                        if link == 'links':
                            for stance in  x['links']:
                                for y in stance.items():
                                    filteredObj = (y)
                                    Links.append(filteredObj)

        return Links



    def getFilteredWords(self,Components,links = None):

        # provide supporting and attacking argumetns with links if required
        sentences = []
        for (sentiment,words) in Components:
            words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
            sentences.append((words_filtered,sentiment))

        return sentences


    def get_words_in_doc(self,sentences):
        all_words = []
        for (words, sentiment) in sentences:
            all_words.extend(words)
        return all_words


    def get_word_features(self,wordlist):
        wordlist = nltk.FreqDist(wordlist)
        word_features = wordlist.keys()
        return word_features

#--------------------------------------------Test data extraction --------------------------------------#

    def getTestData(self,key):

        doc = reader.documents[key]
        dataObjectList = []
        annotatedData = set(doc.annotations)
        for annotation in annotatedData:
                # print("annotation :", annotation.repr)
                # print("labels :", annotation.labels.items())
                # print("links :", annotation.links)
                # print("********************************************************************************")

            dataObject = {"annotation": annotation.repr,
                              "labels": annotation.labels.items(),
                              "links": annotation.links}

            dataObjectList.append(dataObject)

        data = self.ExtractTestSentences(dataObjectList)

        return data


    def ExtractTestSentences(self,data):

        sentences = []
        for items in data:
            sentence = items['annotation']
            sentences.append(sentence)

        return sentences


#------------------------------------------utilities -------------------------------------#

    def getPathToFile(self,RelativePath):
        dir = os.getcwd()
        ROOT_DIR = os.path.dirname(os.path.abspath(dir))
        folder = os.path.join(ROOT_DIR, RelativePath)
        return folder

