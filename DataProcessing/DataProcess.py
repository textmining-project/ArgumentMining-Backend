

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
        annotations = []
        labels = []
        links = []
        for items in data:
            print items['annotation']
            sentence = items['annotation']
            for label in items['labels']:
                print ("label:",label)
                for lab in label:
                    print lab
                    if lab != None and lab != []:
                        labelled = {"label": lab}
                        labels.append(labelled)
            for link in items['links'].iteritems():
                print link




