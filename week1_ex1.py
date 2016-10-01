#!/usr/bin/env python

__author__ = 'Will Dennis'
__email__ = 'wdennis@nec-labs.com'


def mean(numbers):
    """Calculates mean value of a list of numbers."""
    return float(sum(numbers)) / max(len(numbers), 1)


USER_NUMBER_LIST = input('Please enter a list of numbers, separated by a comma: ', )

print('Biggest number: {}').format(max(USER_NUMBER_LIST))
print('Smallest number: {}').format(min(USER_NUMBER_LIST))
print('Mean of all numbers: {}').format(mean(USER_NUMBER_LIST))
print('Sorted list of numbers: {}').format(sorted(USER_NUMBER_LIST))
