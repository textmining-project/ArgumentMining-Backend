'''
import nltk
nltk.download('movie_reviews')
nltk.download('stopwords')
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict


neg_reviews = []
for fileid in movie_reviews.fileids('neg'):
    words = movie_reviews.words(fileid)
    neg_reviews.append((create_word_features(words), "negative"))


pos_reviews = []
for fileid in movie_reviews.fileids('pos'):
    words = movie_reviews.words(fileid)
    pos_reviews.append((create_word_features(words), "positive"))

print(len(pos_reviews))
print(len(neg_reviews))

train_set = neg_reviews[:750] + pos_reviews[:750]
test_set =  neg_reviews[750:] + pos_reviews[750:]
print(len(train_set),  len(test_set))

classifier = NaiveBayesClassifier.train(train_set)

accuracy = nltk.classify.util.accuracy(classifier, test_set)
print(accuracy * 100)




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

SentimentClassifiedData = []
for item in predictedData:
    testString = item[0]
    words = word_tokenize(testString)
    words = classification.create_word_features(words)
    sentiment = LinksSentimentClassifier.classify(words)
    x = list(item)
    x.append(sentiment)
    SentimentClassifiedData.append(tuple(x))

print SentimentClassifiedData



sentences = []
        words = []
        sentences.append(nltk.sent_tokenize(data))
        for sentence in sentences[0]:
            words.append(nltk.word_tokenize(sentence))

        return words



claims = []
premises = []
for item in predictedArgData:
    if item[1] == 'Premise':
        x = [item[0],item[1]]
        premises.append(x)
    if item[1] == 'Claim':
        x = [item[0],item[1]]
        claims.append(x)


print claims
print premises

'''
import nltk

para = "First of all, through cooperation, children can learn about interpersonal skills which are significant in the future life of all students. What we acquired from team work is not only how to achieve the same goal with others but more importantly, how to get along with others. During the process of cooperation, children can learn about how to listen to opinions of others, how to communicate with others, how to think comprehensively, and even how to compromise with other team members when conflicts occurred. All of these skills help them to get on well with other people and will benefit them for the whole life.On the other hand, the significance of competition is that how to become more excellence to gain the victory. Hence it is always said that competition makes the society more effective. However, when we consider about the question that how to win the game, we always find that we need the cooperation. The greater our goal is, the more competition we need. Take Olympic games which is a form of competition for instance, it is hard to imagine how an athlete could win the game without the training of his or her coach, and the help of other professional staffs such as the people who take care of his diet, and those who are in charge of the medical care. The winner is the athlete but the success belongs to the whole team. Therefore without the cooperation, there would be no victory of competition."

sentences = []
words = []

sentences.append(nltk.sent_tokenize(para))


for sentence in sentences[0]:
    words.append(nltk.word_tokenize(sentence))

print words