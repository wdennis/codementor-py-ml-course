#!/usr/bin/env python

__author__ = 'Will Dennis'
__email__ = 'wdennis@nec-labs.com'

import csv

# from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

TRUTHS = []
VECTORS = []
PREDICTIONS = []


def vectorize(datapoint):
    age = datapoint['Age']
    sex = datapoint['Sex']
    pclass = int(datapoint['Pclass'])

    if age == '':
        age = 29.5
    else:
        age = float(age)

    if sex == 'male':
        sex = 1
    else:
        sex = 0

    return [age, sex, pclass]


my_file = open('train.csv', mode='r')
my_csv = csv.DictReader(my_file)
for line in my_csv:
    if line['Survived'] == '1':
        TRUTHS.append(True)
    else:
        TRUTHS.append(False)
    myvec = vectorize(line)
    VECTORS.append(myvec)

# print(VECTORS)


# model = LogisticRegression()
model = KNeighborsClassifier(n_neighbors=3, weights='distance')
model.fit(VECTORS, TRUTHS)

my_file = open('train.csv', mode='r')
my_csv = csv.DictReader(my_file)
for line in my_csv:
    v = vectorize(line)
    PREDICTIONS.append(model.predict([v]))

# print(PREDICTIONS)

correct = 0.0
l = len(PREDICTIONS)
for x in range(l):
    if PREDICTIONS[x] == TRUTHS[x]:
        correct += 1

print('% correct answers: {}').format(correct / len(PREDICTIONS))
