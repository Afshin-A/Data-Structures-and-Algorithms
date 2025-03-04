from abc import ABC, abstractmethod
import math
'''

A heap is a tree that satisfies either of the two properties:
- max heap is a tree where the parent node is greater or equal than its child nodes
- min heap is a tree where the parent node is smaller or equal than its child nodes
Note: A tree cannot include cycles

construction O(n)
polling O(log(n))
adding O(log(n))
peeking O(n)
Naive remove O(n)
Advanced remove (using hash tables) O(log(n))
Naive contains O(n)
Advanced contains O(log(n))
'''

class Heap(ABC):
    '''This is an abstract blue print for the MaxHeap and MinHeap classes
    '''
    def __init__(self, array: list[int]):
        self._heap = array
        self._heap_size = len(array)
    
    @abstractmethod
    def bubble_down(self, i: int):
        pass
    
    @abstractmethod
    def bubble_up(self, i: int):
        pass
    
    @abstractmethod
    def bubble_down(self, i: int):
        pass
    
    def _swap(self, i: int, j: int):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
        # TODO: add code to swap indices inside the hashmap as well
    
    def _build(self):
        '''
        O(n) - time complexity is indeed O(n), not O(nlog(n)). Refer to notes
        For all internal elements in the heap, this function bubbles that element down until the heap invariant property is reached.
        '''
        # formula to get indices of leave nodes of a nearly complete binary tree:
        # range(floor(len(heap)/2), heap_size
        
        # for all internal nodes
        internal_nodes = range(self._heap_size // 2, -1, -1)
        for node in internal_nodes:
            self.bubble_down(node)
    
    def peek(self):
        '''O(1)
        Returns the head element
        '''
        return self._heap[0]
    
    @abstractmethod
    def remove(self, element: int):
        pass
    
    def add(self, element: int):
        self._heap.append(element)
        self._heap_size += 1
        self.bubble_up(self._heap_size - 1)
    
    def pop(self):
        '''O(log(n))
        Removes and returns the top most element
        '''
        # replace the first and last elelemt
        self._swap(0, -1)
        # remove the last element
        max = self._heap.pop(-1)
        self._heap_size -= 1
        
        # restore the heap property
        self.bubble_down(0)
        
        # remove and return the last element
        return max
    
    def contains(self, element):
        '''O(n)
        This is a linear operation. We search through every element in the array. A better method exists using
        hash tables.
        '''
        return self._heap.__contains__(element)   
                
    def contains_advanced(self, element: int):
        '''O(1)
        This method uses hash tables to find and return the index of the first occurence of the argumented value
        using constant time.
        Ideal for when removing lots of elements, however adds overhead
        '''
        pass
    
    def remove_advanced(self, element: int):
        pass
    
    def merge(self, o: 'Heap'):
        '''O(n+m), where m is the size of the other heap
        '''
        self._heap += o._heap
        self._build
    
    
    def is_empty(self):
        return self._heap_size == 0
    
    def size(self):
        return self._heap_size
    
    def __str__(self):
        return str(self._heap)
 
    def __getitem__(self, i):
        if i >= self._heap_size or i < 0:
            raise IndexError
        return self._heap[i]
    
    def __len__(self):
        return len(self._heap)

    def num_internal_nodes(self):
        '''Returns the number of internal nodes in the complete heap
        '''
        # return math.floor(self._heap_size / 2)
        return (self._heap_size // 2) - 1
    
    def num_leaf_nodes(self):
        '''Returns number of leaf nodes in the complete heap
        '''
        # return math.ceil(self._heap_size / 2)
        return (self._heap_size + 1) // 2
    


class MaxHeap(Heap):
    def __init__(self, array: list[int]):
        super().__init__(array)
        self._build()
    
    def bubble_down(self, i: int):
        '''O(log(n))
        Recursively bubbles down an element (with the given index) in the heap (array) until the max-heap property is achieved
        '''
        # print(f'calling max_heapify on node {self._heap[i]}')
        l = i * 2 + 1
        r = l + 1
        largest = i
        
        # find index between the elements parent, left child, or right child
        if l < self._heap_size:
            if self._heap[l] > self._heap[largest]:
                largest = l
        if r < self._heap_size:
            if self._heap[r] > self._heap[largest]:
                largest = r
        
        # if i hasn't changed, that means the given node is the larger than its children and it's at the right spot
        # otherwise, we want to recursively call the function and bubble down the node until it's at the right place
        if i != largest:
            # swap elements in the array
            self._swap(i, largest)
            # recursive call
            self.bubble_down(largest)
            
    def bubble_up(self, child_index):
        parent_index = (child_index - 1) // 2
        # if child is equal to the parent, the heap property would still be intact
        # only if the child is larger than the parent do we need to swap
        if self._heap[child_index] > self._heap[parent_index]:
            self._swap(child_index, parent_index)
            self.bubble_up(parent_index)
            
    def remove(self, element: int):
        '''O(n)
        Removes the first occurence of the given element
        '''
        # list.index() performs a linear search and therefore has a time complexity of O(n).
        index = self._heap.index(element)
        self._swap(index, self._heap_size-1)
        self._heap.pop()
        self._heap_size -= 1
        parent = (index - 1) // 2
        
        # if index is 0, parent would be -1
        if parent < 0:
            self.bubble_down(index)
        elif self._heap[parent] < self._heap[index]:
            self.bubble_up(index)
        else:
            self.bubble_down(index)
        # just because
        return index

    def _negate_heap(self):
        '''Helper method that negates all values in the heap if they're integers
        O(n)
        '''
        self._heap = [-node for node in self._heap]
            
    def minimize(self):
        '''
        Converts the max heap to a min heap
        '''
        self._negate_heap()
        self._build()
        self._negate_heap()
        

    

    
class MinHeap(Heap):
    def __init__(self, array: list[int]):
        super().__init__(array)
        self._build()
        
    def bubble_down(self, i: int):
        l = i * 2 + 1
        r = l + 1
        smallest = i
        
        if l < self._heap_size and self._heap[l] < self._heap[smallest]:
            smallest = l
        if r < self._heap_size and self._heap[r] < self._heap[smallest]:
            smallest = r
        
        if i != smallest:
            self._heap[i], self._heap[smallest] = self._heap[smallest], self._heap[i]
            self.bubble_down(smallest)
            
    def bubble_up(self, child_index: int):
        parent_index = (child_index - 1) // 2
        if self._heap[parent_index] > self._heap[child_index]:
            self._swap(child_index, parent_index)
            self.bubble_up(parent_index)
    
    def remove(self, element: int):
        '''O(n)
        Removes the first occurence of the given element
        '''
        # list.index() performs a linear search and therefore has a time complexity of O(n).
        index = self._heap.index(element)
        self._swap(index, self._heap_size-1)
        self._heap.pop()
        self._heap_size -= 1
        parent = (index - 1) // 2
        
        if parent <= 0:
            self.bubble_down(index)
        elif self._heap[parent] > self._heap[index]:
            self.bubble_up(index)
        else:
            self.bubble_down(index)
        
        return index
        


def heap_sort(array: list[int]):
    '''O(nlog(n))
    We first build a max heap. Then, we pop and store the head (because that is the largest element). We then restore 
    the heap property, and repeat this process until all elements in the heap are removed.
    '''
    heap = MaxHeap(array)
    results = []
    
    for _ in range(len(heap)-1, -1, -1):
        max = heap.pop()
        results.append(max)
        
    return results


# l = [0, 9, 8, 6, 4, 3, 7, 5, 1, 3]
# print(list(range(len(l))))
# max_heapify(len(l), l, 0)
# print('l:', l)
# heap = MaxHeap(l)
# print('heap:', heap)

# print(heap.pop())
# print(heap)
# print(len(heap))

# # heap = Heap(l)
# print(heap)
# print()

# print(heap.heap_sort())
# print(heap.heap_sort_fix())

# num_nodes = 11
# print(num_nodes - math.floor(num_nodes / 2))

# print(heap_sort(l))


# heap.remove(3)
# heap.minimize()
# print('heap:', heap)

# heap.add(10)

# print(heap)


