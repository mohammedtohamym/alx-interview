#!/usr/bin/python3
"""Module defining isWinner function."""


def primeNumbers(n):
    """This function returns a list of prime numbers
    smaller or equal to n using the Sieve of Eratosthenes."""
    primes = []
    is_prime = [True] * (n + 1)
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes

def isWinner(x, nums):
    """
    This shows the winner
    """

    if x != len(nums):
        return None

    ben_score = 0
    maria_score = 0

    for num in nums:
        primes = primeNumbers(num)
        if len(primes) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1
    if ben_score > maria_score:
      return "Ben"  
    else:
      return "Maria"
