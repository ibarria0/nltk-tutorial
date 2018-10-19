import random
import nltk
import csv
from nltk.corpus import stopwords
stop_words = set(stopwords.words('spanish'))

def tokenize(doc):
    tokens = nltk.word_tokenize(doc.lower())
    ##remove stopwords
    ##remove non alphanumeric
    #posiblemente agregar NGRAMS (aveces es peor)
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
random.shuffle(data)

#quitamos las otras columnas
documents = [(doc.lower(),tag) for url,titulo,doc,source,tag in data]

#tokenization
documents = [(tokenize(doc),tag) for doc,tag in documents]

#aqui deben sacar la lista de todas las palabras entre todos los docs para el bag of words
all_words = nltk.FreqDist('array con todos los tokens')
word_features = list(all_words)[:2000]

#poner documentos en el formato que acepta el clasificador ([caracteristicas],'tag')
#tienen que usar la funciona para extraer las caracteristicas (document_features())
featuresets = []

train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set))
print(classifier.show_most_informative_features(50))
