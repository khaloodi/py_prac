#!/usr/bin/env python

"""
Create a generic hash map class from scratch
"""

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # current_array_value currently holds different key
    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
      return None
    elif possible_return_value[0] == key:
      return possible_return_value[1]

    return self.array[array_index]



#### Test Case ####
hash_map = HashMap(20) #creating hashmap of array size 20
hash_map.assign("gneiss", "metamorphic") #store a key/value
print(hash_map.retrieve("gneiss")) #retrive that value