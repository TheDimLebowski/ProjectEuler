"""Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""
from p3 import is_prime

def nth_prime(n):
    p = []
    i = 0
    while len(p)<n:
        i+=1
        if is_prime(i):
            p.append(i)
    return p[-1]

print map(nth_prime,[6,10001])
