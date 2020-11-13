import numpy as np
import time


def compute_triangle_number(idx, prev_num=0, prev_sum=0):
    """"
    This function would return the triangle number of the index 'idx' along with the previous
    triangle number
    """
    if prev_num <= idx:
        return np.array((range(prev_num+1, idx + 1))).sum() + prev_sum
    else:
        return prev_sum - np.array((range(prev_num, idx, -1))).sum()


def compute_factors(t_num):
    """
    Compute the multiplication factors of the given triangle number
    two shortcuts:
    - Consider factors only up to square root of the number given
    - If t_num is odd, then one can disregard all even numbers from factors
    """
    factors = []
    step_size = 1
    if t_num % 2 == 1:
        step_size = 2

    for x in range(1, int(np.sqrt(t_num)) + 1, step_size):
        if not t_num % x:
            factors.append(x)
            quotient = t_num // x
            if quotient > np.sqrt(t_num):
                factors.append(quotient)
    return factors


def find_triangle_num_factors(num_min_factors):
    """
     Finds the first triangle number whose number of factors attains the num_min_factors
     """
    init_num = 1
    prev_t_num = 0
    while True:
        triangle_num = compute_triangle_number(init_num, init_num - 1, prev_t_num)
        triangle_factors = compute_factors(triangle_num)
        if len(triangle_factors) >= num_min_factors:
            break
        init_num += 1
        prev_t_num = triangle_num

    return triangle_num

    # Find the triangle number that has more than num_min_factors factors

    # Calculate triangle numbers
    # Calculate the factors of each triangle number
    # Calculate the number of factors
    # Check if this number if greater than num_min_factors
    # If yes, we stop and return the triangle number


startT = time.time()
print(find_triangle_num_factors(500))
endT = time.time()
print(endT - startT)