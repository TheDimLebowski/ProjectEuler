"""Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

def get_largest_palindrome(n):
    max_N = 10**n
    pal = []
    for i in range(max_N):
        for j in range(max_N):
            p = i*j
            if p == int(str(p)[::-1]):
                pal.append(p)
    return max(pal)

if __name__ == "__main__":
    print get_largest_palindrome(3)
