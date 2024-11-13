#!/usr/bin/env python3
from math import factorial


def pascal_triangle(n):
    result = []
    num = 0
    if n <= 0:
        return result
    for r in range(n):
        row = []
        k = 0
        while (k <= r):
            row.append(int(factorial(r) / (factorial(k)*factorial(r-k))))
            k += 1
        result.append(row)
    return (result)
