from math import sqrt

# Stretch goal: The Sieve of Eratosthenes


class Sieve(object):
    stop = None
    collection = None

    def __init__(self, n):
        self.stop = sqrt(n)
        self.collection = [x for x in range(2, n+1)]


class Eratosthenes(Sieve):
    last_prime = None
    primes = []

    def __init__(self, n):
        super().__init__(n)
        self.last_prime = self.collection[0]
        self.run()

    def next_prime(self):
        if (self.last_prime > self.stop):
            return False
        self.collection = self.filterMultiplesOf(self.last_prime)
        self.primes.append(self.last_prime)
        self.last_prime = self.collection[0]
        return True

    def filterMultiplesOf(self, num):
        def foo(bar): return bar % num != 0
        return list(filter(foo, self.collection))

    def run(self):
        getPrime = True
        while getPrime:
            getPrime = self.next_prime()
        self.primes += self.collection
        self.collection = []
        return True


# print all prime numbers less than 2020
soe = Eratosthenes(2020)
print(soe.primes)
