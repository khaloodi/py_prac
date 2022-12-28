#!/usr/bin/env python

"""
Blossom
The language of the flowers has a long history and has often been a topic resigned
 to the domain of dusty books in a thrift bookseller or a library.
  With Blossom, we want to give people lightning fast access to all of the 
  possible meanings of their favorite flowers.

In this project, we are going to implement a hash map to relate the names 
of flowers to their meanings. In order to avoid collisions when our hashing
 function collides the names of two flowers, we are going to use separate 
 chaining. We will implement the Linked List data structure for each of 
 these separate chains.
"""
from linked_list import Node, LinkedList

class HashMap:

    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for num in range(size)]

    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code%self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.compress(key))
        # self.array[array_index] = [key, value]
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        for item in list_at_array:
            if key == item[0]:
                item[1] = value
                return 
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        # payload = self.array[array_index]
        list_at_index = self.array[array_index]

        # if payload is not None and payload[0] == key:
        #     return payload[1]
        # else:
        #     return None
        for item in list_at_index:
            if key == item[0]:
                return item[1]
        return None
