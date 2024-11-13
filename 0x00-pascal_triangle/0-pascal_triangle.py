#!/usr/bin/python3
'''Create a function def pascal_triangle(n):'''


def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def pascal_triangle(n):
    '''
    Returns a list of lists of integers
    Returns an empty list if n <= 0
    '''
    result = []
    if (type(n) is not int) or (n <= 0):
        return result
    for r in range(n):
        row = []
        k = 0
        while (k <= r):
            row.append(int(iterative_factorial(r) /
                           (iterative_factorial(k)*iterative_factorial(r-k))))
            k += 1
        result.append(row)
    return (result)
