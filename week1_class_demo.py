#!/usr/bin/env python

__author__ = 'Will Dennis'
__email__ = 'wdennis@nec-labs.com'

mysum = 0.0

numbers_to_average = [45, 90, 86, 100, 76]

for x in numbers_to_average:
    mysum = mysum + x

ave = mysum / len(numbers_to_average)
print(ave)

if ave >= 60:
    print('you pass!')
else:
    print('you failed!')