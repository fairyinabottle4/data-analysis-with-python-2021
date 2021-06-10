#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np
from numpy.core.numeric import cross

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    features = np.zeros((len(a), 29))
    #for each row, the number of occurences of a certain character in each word is listed
    for i, word in enumerate(a):
        for j, char in enumerate(alphabet):
            features[i, j] += word.count(char)

    return features

def contains_valid_chars(s):
    for char in s:
        if char not in alphabet:
            return False
    return True

def get_features_and_labels():
    #the remaining words must all be converted to lower case
    finnish = load_finnish()
    finnish = [i.lower() for i in finnish]
    finnish = [x for x in finnish if contains_valid_chars(x)]

    english = load_english()
    english = [x for x in english if x[0].islower()]
    english = [i.lower() for i in english]
    english = [x for x in english if contains_valid_chars(x)]

    finnish_features = get_features(finnish)
    english_features = get_features(english)
    X = np.concatenate((finnish_features, english_features))

    y = np.zeros(len(finnish)+len(english))
    # 1 for english, 0 for finnish
    y[len(finnish): ] = 1
    return (X, y)                        

def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()
    #this is a less precise version, because the default shuffle is false, 
    # which means that the splits are the same across all 5 calls 
    #scores = cross_val_score(model, X, y, cv=5)

    gen = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    scores = cross_val_score(model, X, y, cv=gen)
    return scores


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
