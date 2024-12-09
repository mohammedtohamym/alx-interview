#!/usr/bin/python3
"""Module defining isWinner function."""


def isWinner(x, nums):
    """Function to determine the winner of the prime game."""
    maria_wins = 0
    ben_wins = 0

    for num in nums:
        rounds = list(range(1, num + 1))
        primes = find_primes(num)

        if not primes:
            ben_wins += 1
            continue

        maria_turn = True

        while primes:
            current_prime = primes.pop(0)
            rounds = [n for n in rounds if n % current_prime != 0]

            if not rounds:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            maria_turn = not maria_turn

    if maria_wins > ben_wins:
        return "Winner: Maria"
    elif ben_wins > maria_wins:
        return "Winner: Ben"
    return None


def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primes(limit):
    """Generate a list of prime numbers up to a given limit."""
    return [n for n in range(2, limit + 1) if is_prime(n)]

