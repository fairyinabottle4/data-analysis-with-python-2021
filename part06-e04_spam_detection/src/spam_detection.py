#!/usr/bin/env python3

from gzip import open
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

from sklearn.feature_extraction.text import CountVectorizer

def spam_detection(random_state=0, fraction=1.0):
    #following lines are for reading data
    list_ham = None
    list_spam = None
    ham_file = 'src/ham.txt.gz'
    spam_file = 'src/spam.txt.gz'
    with open(ham_file) as ham_data:
        list_ham = ham_data.readlines()
        num_lines = int(fraction * len(list_ham))
        list_ham = list_ham[:num_lines]
    with open(spam_file) as spam_data:
        list_spam = spam_data.readlines()
        num_lines = int(fraction * len(list_spam))
        list_spam = list_spam[:num_lines]    
    vec = CountVectorizer()  

    #the following block of steps are always necessary to form the entire set
    X_rows = list_ham + list_spam  
    X = vec.fit_transform(X_rows).toarray()
    # label 1 for spam
    y = np.zeros(len(X_rows))
    y[len(list_ham):] = 1

    #the set formed above is then transformed into training and test sets
    #this is pretty standard, similar to the previous exercises
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=random_state)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_fitted = model.predict(X_test)
    result = accuracy_score(y_test, y_fitted)
    misclassified = np.sum(y_test != y_fitted)
    return (result, len(X_test), misclassified)

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
