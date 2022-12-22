#!/usr/bin/env python

"""
Build a stack data structure
"""

from node import Node

# Add your Stack class below:
class Stack:
  def __init__(self):
    self.top_item = None
    
  def peek(self):
    return self.top_item.get_value()