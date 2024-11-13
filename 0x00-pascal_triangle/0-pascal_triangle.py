#!/usr/bin/env python3

def iterative_factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def pascal_triangle(n):
    result = []
    num = 0
    if n <= 0:
        return result
    for r in range(n):
        row = []
        k = 0
        while (k <= r):
            row.append(iterative_factorial(r) / (iterative_factorial(k)*iterative_factorial(r-k)))
            k += 1
        result.append(row)
    return (result)
