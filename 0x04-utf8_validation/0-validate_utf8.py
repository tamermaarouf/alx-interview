#!/usr/bin/python3
'''
Write a method that determines if a given data set represents a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
'''


def validUTF8(data):
    binary_data = []
    for dt in data:
        binary_data.append(dec2bin(dt))
    return binary_data
    pass

def dec2bin(number: int):
    ans = ''
    if ( number == 0 ):
        return 0
    while ( number ):
        ans += str(number&1)
        number = number >> 1

    ans = ans[::-1].zfill(8)
    print(f'---{ans}')
    return ans
