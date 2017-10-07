import collections
from itertools import ifilter

class DataProcess(object):
    def __init__(self):
        pass


    def ProcessData(self,annotations):
        dataObjectList = []
        annotatedData = set(annotations)
        for annotation in annotatedData:
            #print("annotation :", annotation.repr)
            #print("labels :", annotation.labels.items())
            #print("links :", annotation.links)
            #print("********************************************************************************")

            dataObject = {"annotation": annotation.repr,
                          "labels": annotation.labels.items(),
                          "links": annotation.links}

            dataObjectList.append(dataObject)
            #print(len(dataObjectList))


        self.ExtractDataFeatures(dataObjectList)


    def ExtractDataFeatures(self,data):
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



        print wholeobject



