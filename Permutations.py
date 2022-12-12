#!/usr/bin/env python

"""
In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

* With input 'a'
* Your function should return: ['a']
* With input 'ab'
* Your function should return ['ab', 'ba']
* With input 'aabb'
* Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.
"""

from itertools import permutations
from itertools import combinations

l1 = 'a'
l2 = 'ab'
l3 = 'aabb'

def permutation(s):
    perm = permutations(s)
    combos = list(combinations(s,1))
    print('Combos count: ', len(combos))
    array = []

    for i in set(perm):
        myTuple = i
        x = "".join(myTuple)
        # array.append(list(i).join(','))
        array.append(x)

    return array

# print(permutation(l1))
# print(permutation(l2))
print(permutation(l3))