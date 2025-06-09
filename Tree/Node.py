from functools import total_ordering
# To reduce boiler plate code, total_ordering will generate all comparison methods based on __le__ and __eq__ methods
from typing import Self

@total_ordering
class Node:
    '''Node class specifically used for binary trees
    Naming convention makes intuition easier
    '''
    def __init__(self, data:any=None, parent:'Node'=None, left:'Node'=None, right:'Node'=None, height=0):
        self.parent: Node = parent
        self.left: Node = left
        self.right: Node = right
        self.data: int = data
        self.update(height)

    def update(self, height):
        self.height = height
        rightHeight = 0
        leftHeight = 0
        if self.right:
            rightHeight = self.right.height
        if self.left:
            leftHeight = self.left.height
        self.balance_factor = rightHeight - leftHeight
        
    def __str__(self):
        return str(self.data)
    
    def __eq__(self, other: 'Node'):
        return isinstance(other, Node) and self.data == other.data
    
    def __le__(self, other: 'Node'):
        return isinstance(other, Node) and self.data < other.data
