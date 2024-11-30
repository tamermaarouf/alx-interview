#!/usr/bin/python3
'''
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste.
Given a number n, write a method that calculates the fewest
number of operations needed to result in exactly n H characters in the file.
Prototype: def minOperations(n)
'''


def minOperations(n):
    '''Returns an integer
    If n is impossible to achieve, return '''
    if n < 2:
        return 0
    factor = 2
    while n % factor != 0:
        factor += 1
    return factor + minOperations(n//factor)
