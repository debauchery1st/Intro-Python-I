from sys import argv
from sieve import Eratosthenes

# start with the list of primes under 50
primesUnder50 = Eratosthenes(50).primes

# Stretch goal: Write a program to determine if a number, given on the command line, is prime.


def is_prime(n):
    if n < 50:
        return n in primesUnder50
    # make a new sieve when n is greater than 50
    return n in Eratosthenes(n).primes


def interactive(num=None):
    if (num is None):
        num = input("Enter a number: ")
    try:
        num = int(num)
        if is_prime(num):
            print("Prime")
        else:
            print("not prime")
    except ValueError as ve:
        print(ve)


if __name__ == "__main__":
    if len(argv) < 2:
        interactive()
    else:
        try:
            n = int(argv[1])
            interactive(n)
        except ValueError as ve:
            print(ve)
