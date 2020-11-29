"""
This problem comes from https://projecteuler.net/problem=9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import numpy as np
import time

# Multiple pieces of the problem
# 1. Check if a given set of three numbers form a pythagorean triplet
# 2. Check if the sum of the pythogorean triplet is 1000, if so, compute product.
# 3. Generate three numbers optimally.
# 1. and 2. can be put together.
# 1. and 3. can be put together if we only focus on generating pythagorean triplets
#
# What is the range for which we should go on?
#   - definitely less than 1000
#   -


def check_square(num):
    """
    Given the number num, the function will return whether its integer square root
    or -1.
    """
    c = np.sqrt(num)
    if c.is_integer():
        return c
    else:
        return -1


def check_pythagorean_triplet(a, b):
    """
    Given two numbers a, b check if they form a Pythagorean triplet along with
    the sum of their squares
    """
    c_sq = a**2 + b**2

    c = check_square(c_sq)

    if c == -1:
        return -1
    else:
        return c


def check_sum_of_triplets(a, b, c):
    """
    Check if the three have a sum 1000.
    """
    if a + b + c == 1000:
        return a*b*c
    else:
        return -1


def main():
    """
    The main function where we go around to check for values
    """
    for i in list(range(1, 400)):
        for j in list(range(i+1, 450)):
            k = check_pythagorean_triplet(i, j)
            if k == -1:
                continue
            else:
                prod_val = check_sum_of_triplets(i, j, k)
                if prod_val == -1:
                    continue
                else:
                    print(i, j, k, prod_val)
                    break


tic = time.process_time()
main()
toc = time.process_time()
print(toc-tic)
