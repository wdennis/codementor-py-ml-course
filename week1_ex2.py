#!/usr/bin/env python

__author__ = 'Will Dennis'
__email__ = 'wdennis@nec-labs.com'


def mean(numbers):
    """Calculates mean value of a list of numbers."""
    return float(sum(numbers)) / max(len(numbers), 1)


def print_student_stats(student, gradeset):
    """Prints student name, then max / min / mean / list of test scores."""
    # TODO: Write logic to vet scores for validity, i.e. score > 0, and score < 100
    print('Student name: {}').format(student)
    print('Highest score: {}').format(max(gradeset))
    print('Lowest score: {}').format(min(gradeset))
    print('Mean of all scores: {}').format(mean(gradeset))
    print('Sorted list of scores: {}\n').format(sorted(gradeset))


grades = {
    'Ben': [80, 90, 100],
    'Zach': [70, 85, 50],
    'Meghan': [100, 90, 15, 90]
}

for k, v in grades.items():
    print_student_stats(k, v)
