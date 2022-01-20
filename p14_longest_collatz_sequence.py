"""
This file solves the problem 14 of the Euler project:
https://projecteuler.net/problem=14
"""
import numpy as np

def collatz_update(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n+1

# collatz_chain_data = {"1": }

start_num = 1
collatz_chain_len = 1
for i in range(2, 1000001):
    chain_len = 1
    num = i
    while num > 1:
        num = collatz_update(num)
        chain_len = chain_len + 1
    if chain_len > collatz_chain_len:
        collatz_chain_len = chain_len
        start_num = i

print("The number with the longest chain is: ", start_num)
print("The longest chain length is:", collatz_chain_len)
