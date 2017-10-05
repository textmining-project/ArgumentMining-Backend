import classifier as classifier
import nltk
import bratreader
import Splitter
import POSTagger
import DataProcessing

from DictionaryTagger import DictionaryTagger
from bratreader.repomodel import RepoModel
from DataProcessing import DataProcess




reader = RepoModel("bratessays") # load repomodel
reader.documents

doc = reader.documents["essay01"]		# get document with key 001
#print("sentences",doc.sentences)    			# a list of sentences in document
#print("annotation :",doc.annotations)       # the annotation objects in a documennt


p = DataProcess.DataProcess()
p.ProcessData(doc.annotations)

"""
splitter = Splitter.Splitter()
postagger = POSTagger.POSTagger()

splitted_sentences = splitter.split()

print(splitted_sentences)

pos_tagged_sentences = postagger.pos_tag(splitted_sentences)

print pos_tagged_sentences


dicttagger = DictionaryTagger(['Dictionary/Claim.yml','Dictionary/Premise.yml'])

dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)

print(dict_tagged_sentences)


"""


