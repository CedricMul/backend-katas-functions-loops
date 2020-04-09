#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """
import operator

__author__ = "Cedric Mulvihill"


def add(x, y):
    """Add two integers. Handles negative values."""
    a = x + y
    return a


def multiply(x, y):
    mult_list = []
    a = 0
    """Multiply x with y. Handles negative values of x or y."""
    if x != 0 and y != 0:
        for i in range(abs(x)):
            mult_list.append(abs(y))
        for i in mult_list:
            a = add(a, i)
        if (x < 0 and y > 0) or (x > 0 and y < 0):
            a = operator.neg(a)
    return a

def power(x, n):
    """Raise x to power n, where n >= 0"""
    power_list = []
    d = x
    for i in range(n):
        power_list.append(x)
    for i in power_list[1:]:
        d = multiply(d,power_list[i])
    return d


def factorial(x):
    """Compute factorial of x, where x > 0"""
    fact = []
    a = 0
    b = 0
    for i in range(1, add(x, 1)):
        fact.append(i)
    a = fact[0]
    b = fact[1]
    for i in fact[2:]:
        a = multiply(a, b)
        b = i
    a = multiply(a, b)
    return a


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    a = 0
    b = 1
    c = 1
    h = 0
    l = []
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        for i in range(3, add(n,1)):
            h = c
            c = add(b,c)
            a = b
            b = h
    return c


if __name__ == '__main__':
    print(add(2, 4))
    print(multiply(6, -8))
    print(power(2, 8))
    print(factorial(4))
    print(fibonacci(8))
