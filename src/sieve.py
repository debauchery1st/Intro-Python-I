from math import sqrt
from sys import argv

# Stretch goal: The Sieve of Eratosthenes


class Sieve(object):
    collection = None

    def __init__(self, n):
        self.collection = [x for x in range(2, n+1)]

    def sift(self, customFilter=None):
        if customFilter is None:
            return
        return list(filter(customFilter, self.collection))


class Eratosthenes(Sieve):
    last_prime = None
    stop = None
    primes = []

    def __init__(self, n):
        super().__init__(n)
        self.stop = sqrt(n)
        self.last_prime = self.collection[0]
        self.run()

    def next_prime(self):
        if (self.last_prime > self.stop):
            return False
        self.collection = self.sift(lambda x: x % self.last_prime != 0)
        self.primes.append(self.last_prime)
        self.last_prime = self.collection[0]
        return True

    def run(self):
        getPrime = True
        while getPrime:
            getPrime = self.next_prime()
        self.primes = sorted([x for x in set(self.primes + self.collection)])
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
        example()
