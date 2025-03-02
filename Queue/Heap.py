'''
A heap is a tree that satisfies either of the two properties:
- max heap is a tree where the parent node is greater or equal than its child nodes
- min heap is a tree where the parent node is smaller or equal than its child nodes
Note: A tree cannot include cycles
'''

'''
in a minimum priority queue, smaller values have higher priority, so they come out of the queue first
in a maximum priority queue, larger values come out first
'''

'''
Priority queue is an abstract data type that can be implemented using different data structures, however heaps provide
the best possible time complexities
'''

from LinkedList.Node import Node


class BinaryHeap:
    def __init__(self, data):
        # is this a maximum binary heap?
        self._maximum = True
        self._root = data
        self._size = 1
        # should we allow the user to select if they want a max or min heap?
        
        
        
    
    def poll(self):
        '''Remove the element at the root.\n
        O(log(n))
        '''
        raise NotImplementedError
        
    def remove(self, data):
        '''Find the node with the given data, then remove it.\n
        O(n)
        '''
        # linearly search for data: find the top left most node with the given data
        # swap it with the last (right most) element
        # remove the node
        # bubble-up or down the swapped node until the heap property is valid
        
        # we can also use a hashmap or hashtree to instantly look up the indices of an element
        
        raise NotImplementedError
    
    def insert(self, data):
        raise NotImplementedError
    
    
    def convertToMaxHeap(self):
        if self._maximum:
            raise Exception('This is already a maximum binary heap.')
        
        raise NotImplementedError
        
        
        
    def convertToMinHeap(self):
        if not self._maximum:
            raise Exception('This is already a minimum binary heap.')
        raise NotImplementedError
    
    def getLeftChildIndex(self, index):
        return 2*index + 1
    
    def getRightChildIndex(self, index):
        return 2* index + 2