import gensim
from scipy import spatial
import numpy as np
import nltk
from Utils import Utils

from DataProcessing import DataProcess


dataProcess = DataProcess.DataProcess()

class RelationAnalyzer(object):

    def __init__(self):
        pass

    def performRelationAnalysis(self,claims,premises):

        claimlist = claims
        premiselist = premises

        essayfile = Utils().getPathToFile('DataProcessing/all_essay.txt')

        file = open(essayfile,"r")
        corpus = file.read()
        file.close()

        tak_corp = [nltk.word_tokenize(corpus) ]

        # ---------- Uncommet this if need to update the model ---#
        #model = gensim.models.Word2Vec(tak_corp,min_count=1,size = 32)
        #model.save('word2Vec.wv')

        model = gensim.models.Word2Vec.load('word2Vec.wv')


        modelset = set(model.wv.index2word)
        result = []
        for claim in claimlist:
            for premise in premiselist:
                sentence_1_avg_vector = self.avg_feature_vector(claim[0].split(), model=model, num_features=32, index2word_set=modelset)
                sentence_2_avg_vector = self.avg_feature_vector(premise[0].split(), model=model, num_features=32, index2word_set=modelset)
                sen1_sen2_similarity = 1 - spatial.distance.cosine(sentence_1_avg_vector, sentence_2_avg_vector)
                if (sen1_sen2_similarity == "nan"):
                    pass
                    #print("not similar")
                else:
                    pass
                    #print(sen1_sen2_similarity * 100)
                result.append([claim[0],premise[0],sen1_sen2_similarity* 100])

        claims = []
        premises = []
        for item in result:
            if item[2] > 99.993:
                claims.append(item[0])
                premises.append(item[1])


        return [claims,premises]


    def avg_feature_vector(self,words, model, num_features, index2word_set):
        # function to average all words vectors in a given paragraph
        featureVec = np.zeros((num_features,), dtype="float32")
        # print (len(featureVec))
        nwords = 0

        # list containing names of words in the vocabulary
        # index2word_set = set(model.index2word) this is moved as input param for performance reasons
        for word in words:
            if word in index2word_set:
                nwords = nwords + 1
                # print(len(model[word]))
                featureVec = np.add(featureVec, model[word])

        if (nwords > 0):
            featureVec = np.divide(featureVec, nwords)
        return featureVec