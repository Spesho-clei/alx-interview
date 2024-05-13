#!/usr/bin/python3
"""Prime game module"""

def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    
    marias_wins, bens_wins = 0, 0
    
    # Generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    
    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
    
    # Count prime numbers for each round and update wins
    for num in nums:
        prime_count = sum(primes[2:num+1])  # Count prime numbers up to num
        if prime_count % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1
    
    # Determine the winner
    if marias_wins == bens_wins:
        return None
    elif marias_wins > bens_wins:
        return "Maria"
    else:
        return "Ben"
