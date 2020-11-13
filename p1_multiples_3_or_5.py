import numpy as np
from time import time as tt


def sum_nums_multiples_of_three_or_five(num):
    """
    project euler problem 1 : Multiples of 3 and 5
    :param num: The number up to which one has to list all the numbers which are multiples of either 3 or 5
    and return their sum
    :return:the sum of all the numbers
    """

    # Step 1: given a number, check each number from 0 until that number if it is divisible by 3 or 5
    # Step 2: If a number of divisible, append it to a list.

    # without numpy
    # num_list = []
    # for x in range(1, num):
    #     if (x % 3 == 0) or (x % 5 == 0):
    #         num_list.append(x)
    #
    # return sum(num_list)

    # with numpy
    num_list_full = np.array(list(range(1, num)))
    num_list_reduced = num_list_full[(num_list_full % 3 == 0) | (num_list_full % 5 == 0)]
    return sum(num_list_reduced)


startT = tt()
print(sum_nums_multiples_of_three_or_five(1000))
endT = tt()
print(endT - startT)

