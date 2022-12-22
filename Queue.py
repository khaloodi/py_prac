#!/usr/bin/env python

"""
Build a queue data structure
"""

from node import Node
# Create the Queue class below:

class Queue(Node):
  def __init__(self):
    self.head = None
    self.tail = None
    
  def peek(self):
    return self.head.get_value()