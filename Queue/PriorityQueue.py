'''
Priority queue is an abstract data type that behaves just like a normal queue, only nodes leave the queue according to their priority.
Each node has a numerical value that tells us its priority. PQs are can be implemented using different data structures such as arrays. However,
the most efficient way are heaps. Heaps are binary trees that follow the heap invariant, i.e. parent elements are >= than their children in a max heap
or that parents are <= than their children in what's called a min heap. PQs are often used in graph theory algorithms, in Huffman coding, or anytime
we need to fetch the next best or next worse element in an application

Priority queue is an abstract data type that can be implemented using different data structures, however heaps provide
the best possible time complexities

in a minimum priority queue, smaller values have higher priority, so they come out of the queue first.
in a maximum priority queue, larger values come out first. We implement this data structure using a maximum heap, as shown in this file
'''

from Heap.Heap import MaxHeap, MinHeap

class PriorityQueue:
    def __init__(self, data: list[int], max=True):
        # is this a maximum binary heap?
        self._queue = None
        if max:
            self._queue = MaxHeap(data)
        else:
            self._queue = MinHeap(data)
        
        # should we allow the user to select if they want a max or min heap?
        
    def size(self):
        return self._queue.size()
    
    def enqueue(self, data):
        return self._queue.add(data)
        
    def add(self, data):
        return self.enqueue(data)
    
    def dequeue(self):
        return self._queue.pop()
    
    def poll(self):
        return self.dequeue()
    
    def peek(self):
        return self._queue.peek()
    
    def contains(self, data):
        return self._queue.contains(data)
    
    def remove(self, data):
        return self._queue.remove(data)
    
    def __getitem__(self, i: int):
        return self._queue.__getitem__(i)
    
    def __str__(self):
        return self._queue.__str__()
    