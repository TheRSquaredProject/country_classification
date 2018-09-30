import os
import spacy
from geotext import GeoText
import spacy

nlp = spacy.load('en')
o=os.getcwd()
print(o)
for i in filter(os.path.isdir, os.listdir(os.getcwd())):
    print(os.path.join(o,i))
    for j in os.listdir(os.path.join(o,i)):
        print(j)
        for k in os.listdir(os.path.join(o,i,j)):
            print(k)
            str = open(os.path.join(o,i,j,k), 'r').read()
            #print(str)
            places = GeoText(str)
            nlp_obama = nlp(str)
            for n in nlp_obama.ents:
                if n.label_=='GPE':
                    print([(n, n.label_) ])
