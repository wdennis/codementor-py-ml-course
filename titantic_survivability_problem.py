#!/usr/bin/env python

__author__ = 'Will Dennis'
__email__ = 'wdennis@nec-labs.com'

import csv

import matplotlib.pyplot as plt
import numpy

my_file = open('train.csv', mode='r')
my_csv = csv.DictReader(my_file)

PREDICTIONS = []
TRUTHS = []
YES = []
NO = []


def predict(datapoint):
    age = datapoint['Age']
    sex = datapoint['Sex']
    pclass = int(datapoint['Pclass'])
    print('{};').format(datapoint['Name']),
    print('Age: {};').format(age),
    print('Sex: {};').format(sex),
    print('Pssngr Class: {}').format(pclass)
    if age == '':
        return True
    else:
        age = float(age)
        if age <= 15:
            return True
        # if over 15, we need to decide some other way
        else:
            if sex == 'female':
                return True
            else:
                if pclass == 1:
                    return True
                else:
                    return False


for line in my_csv:
    age = line['Age']
    if line['Survived'] == '1':
        TRUTHS.append(True)
    else:
        TRUTHS.append(False)
    if age == '':
        pass
    else:
        pclass = line['Pclass']
        if line['Survived'] == '1':
            YES.append(int(pclass))
        else:
            NO.append(int(pclass))

    mypred = predict(line)
    PREDICTIONS.append(mypred)
    print("Prediction was: {}").format(mypred)
    print('-----')

correct = 0.0
l = len(PREDICTIONS)
for x in range(l):
    if PREDICTIONS[x] == TRUTHS[x]:
        correct += 1

print('% correct answers: {}').format(correct / len(PREDICTIONS))

print('Mean passenger class of survivors: {}').format(numpy.mean(YES))
print('Mean passenger class of victims: {}').format(numpy.mean(NO))

yes_hist = numpy.histogram(YES)
no_hist = numpy.histogram(NO)

for x in range(len(no_hist)):
    print yes_hist[x] - no_hist[x]

# print('--- YES ---')
# plt.hist(YES, bins=3)
# plt.show()
# print('--- NO ---')
# plt.hist(NO, bins=3)
#plt.show()
