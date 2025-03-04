from functools import total_ordering
# To reduce boiler plate code, total_ordering will generate all comparison methods based on __le__ and __eq__ methods

@total_ordering
class Node:
    def __init__(self, data:any=None):
        self.left: Node = None
        self.right: Node = None
        self.data: int = data
        
    def __str__(self):
        return str(self.data)
    
    def __eq__(self, other: 'Node'):
        return isinstance(other, Node) and self.data == other.data
    
    def __le__(self, other: 'Node'):
        return isinstance(other, Node) and self.data < other.data
