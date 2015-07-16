"""Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

from p3 import is_prime

def primes(max_val):
    p = [2]
    i = 2
    while p[-1]<max_val:
        i+=1
        if is_prime(i):
            p.append(i)
    return p[:-1]

print sum(primes(2e6))
