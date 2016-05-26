"""This module gives basic prime number functions."""

import math
import itertools

def is_prime(number):
    """Checks if a number is prime"""
    if number <= 1:
        return False
    if number == 2:
        return True
    else:
        maximum = int(math.sqrt(number)) + 1
        for i in range(2, maximum):
            if number % i == 0:
                return False
        return True


def primes_gen():
    """Generator of prime numbers"""
    for number in itertools.count(2):
        if is_prime(number):
            yield number
