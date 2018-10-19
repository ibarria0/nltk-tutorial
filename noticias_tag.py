import random
import nltk
import csv
from nltk.corpus import stopwords
stop_words = set(stopwords.words('spanish'))

def tokenize(doc):
    tokens = nltk.word_tokenize(doc.lower())
    #tokens = [t for t in tokens if t not in stop_words] #remove stopwords
    #tokens = [t for t in tokens if t.isalpha()] #remove non alphanumeric
    #tokens = nltk.ngrams(tokens,1)
    #tokens = [stem(t) for t in tokens]
    return tokens

def stem(token):
    pass

def document_features(document,word_features):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

with open('noticias.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))

#quitamos la primera fila, los headers
data = data[1:]

#quitamos las otras columnas
documents = [(doc.lower(),tag) for url,titulo,doc,source,tag in data]

#tokenization
documents = [(tokenize(doc),tag) for doc,tag in documents]

all_words = nltk.FreqDist([token for doc,tag in documents for token in doc])
word_features = list(all_words)[:200]

#cargar data y poner en el formato que acepta el clasificador ([caracteristicas],'tag')
random.shuffle(documents)
featuresets = [(document_features(d,word_features), c) for (d,c) in documents]

train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(50))
