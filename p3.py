"""Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

from math import sqrt; from itertools import count, islice

def is_prime(n):
    if n < 2: return False
    return all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def get_prime_factors(n):

    if n == 1:
        return []

    # Get all factors
    f = []
    max_i = int(n**0.5)+1
    for i in range(2,max_i)[::-1]:
        if (n%i)==0:
            f.append(i)
            f.append(n/i)
    # Get prime factors
    pf = []
    for fi in f:
        if is_prime(fi):
            pf.append(fi)

    if len(pf)==0:
        pf.append(n)

    return pf

if __name__ == "__main__":
    print max(get_prime_factors(600851475143))
