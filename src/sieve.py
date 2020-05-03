from math import sqrt
from sys import argv

# Stretch goal: The Sieve of Eratosthenes


class Sieve(object):
    collection = None

    def __init__(self, n):
        # start with a list of integers from 2 through n+1
        self.collection = [x for x in range(2, n+1)]

    def sift(self, customFilter=None):
        if customFilter is None:
            return
        # return a filtered list of unique elements
        return list(set(filter(customFilter, self.collection)))


class Eratosthenes(Sieve):
    last_prime = None
    stop = None
    primes = []

    def __init__(self, n):
        super().__init__(n)  # initialize Sieve
        self.last_prime = self.collection[0]  # start with the first element
        self.stop = sqrt(n)  # stop sifting at the square root of N
        self.sortPrimes()  # run the sifting cycle, then sort the result.

    def next_prime(self):
        if (self.last_prime > self.stop):
            # we are done sifting
            return False
        # remove any numbers divisible by "last_prime"
        self.collection = self.sift(lambda x: x % self.last_prime != 0)
        # update the list of primes we have sifted thus far
        self.primes.append(self.last_prime)
        # remove stored primes from collection
        self.collection = self.sift(lambda x: x not in self.primes)
        # the first element of our sifted collection becomes the next prime
        self.last_prime = self.collection[0]
        return True

    def sortPrimes(self):
        getPrime = True
        while getPrime:
            getPrime = self.next_prime()  # get the next prime ?
        # produce a sorted list of unique primes
        self.primes = sorted(list(set(self.primes + self.collection)))
        return True


def example():
    # print all prime numbers less than 2020
    soe = Eratosthenes(2020)
    print(soe.primes)


help_message = f"""
Stretch Goal: The Sieve of Eratosthene

Usage:
    python {argv[0]} <number>
    
Example:
    python {argv[0]} 42
    {Eratosthenes(42).primes}
"""


if __name__ == "__main__":
    if len(argv) > 1:
        try:
            soe = Eratosthenes(int(argv[1]))
            print(soe.primes)
        except ValueError as ve:
            print(help_message)
    else:
        print(help_message)
