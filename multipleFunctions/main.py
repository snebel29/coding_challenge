#!/usr/bin/python
#-*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

def is_multiplo(n, m):
    if n % m == 0:
        return True
    else:
        return False

# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def if_even(k):
    if int(str(k)[-1]) in list(range(0,10,2)):
        return True
    else:
        return False
    
# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data):
    mini, maxi = data[0], data[0]
    for i in data:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
    return (mini, maxi)

# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.

def total(n):
    return sum([k*k for k in range(1,n)])

# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def total_odd(n):
    return sum([k*k for k in range(1,n,2)])

# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for in-
# dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
# the same element?

def references():
    s = 'myString'
    return s[-5] == s[3]    

# What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

print(list(range(50,80+1,10)))

# What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

print(list(range(8,-9,-2)))

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

print([2**k for k in range(1,9)])

# Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module in-
# cludes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.

def ownchoice(data):
    import random
    return data[random.randrange(len(data))]
    
# Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.

n = [1,2,3,4,5,6,7,8,9]
nn = []
for i in range(1,len(n)+1):
    nn.append(n[(-1*i)])

print(nn)
print(list(reversed(n)))


if __name__ == '__main__':
    #print(is_multiplo(300,5))
    #print(if_even(3))
    #print(if_even(180))
    #print(minmax((22,-2,3,4,15,7,6)))
    #print(total(5))
    #print(total_odd(5))
    #print(references())
    #print(ownchoice([1,2,3,4,5,6]))
    pass
