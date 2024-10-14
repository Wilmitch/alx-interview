#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest number of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 characters: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # total even-divisions by root = total operations
            ops += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller values that divide n evenly
            root -= 1
        # increment root until it divides n evenly
        root += 1
    return ops
