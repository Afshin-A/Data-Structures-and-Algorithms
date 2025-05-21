from functools import total_ordering
# To reduce boiler plate code, total_ordering will generate all comparison methods based on __le__ and __eq__ methods
from typing import Self

@total_ordering
class Node:
    '''Node class specifically used for binary trees
    Naming convention makes intuition easier
    '''
    def __init__(self, data:any):
        self.__init__(data, None, None)
        
    def __init__(self, data:any, left:Self, right:Self):
        self.data = data
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.data)
    
    def __eq__(self, other: 'Node'):
        return isinstance(other, Node) and self.data == other.data
    
    def __le__(self, other: 'Node'):
        return isinstance(other, Node) and self.data < other.data
