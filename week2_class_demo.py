#!/usr/bin/env python

__author__ = 'Will Dennis'
__email__ = 'wdennis@nec-labs.com'

import random

num_to_guess = random.randint(1, 100)

user_input = -1
guess_count = 0

while user_input != num_to_guess:
    user_input = int(raw_input("Please enter your guess: "))
    guess_count += 1
    if user_input > num_to_guess:
        print("Too high!")
    elif user_input < num_to_guess:
        print("Too low!")
    else:
        print("You got it!")

print("This took you {} tries to guess correctly!").format(guess_count)
