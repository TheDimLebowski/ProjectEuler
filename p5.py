"""Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

from p3 import get_prime_factors

def product(l):
    p = 1
    for el in l:
        p*=el
    return p

def get_multiplicity(n,m):
    k = 0
    while (n%m)==0:
        k+=1
        n/=m
    return k


def get_prime_factors_dict(n):
    pf = get_prime_factors(n)
    d = {}
    for p in set(pf):
        d[p] = get_multiplicity(n,p)
    return d

def lcm(l):
    pf = []
    for el in l:
        print el, get_prime_factors_dict(el)
        pf.append(get_prime_factors_dict(el))

    for pf_dict_i in pf:
        for pf_dict_j in pf:
            for key in pf_dict_i.keys():
                if key not in pf_dict_j.keys():
                    pf_dict_j[key] = 0

    keys = pf[0].keys()

    pflcm = {}
    for key in keys:
        pflcm[key] = max([pf_dict_i[key] for pf_dict_i in pf])

    return product([key**pflcm[key] for key in keys])


if __name__ == "__main__":

    print lcm(range(1,10))
    print lcm(range(1,20))
