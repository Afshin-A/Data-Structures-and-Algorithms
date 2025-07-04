from collections import defaultdict
from pprint import pprint

class MinHeap:
    '''
    NOTE: Heap allows duplicate values
    '''
    def __init__(self, heap: list[any], key_fn=lambda x: x):
        self.size = len(heap)
        # .copy() necessary to avoid conflicts since we pass by reference
        self.heap: list[any] = heap.copy()
        
        # this is necessary for priority queue.
        # with this function, we can control what part of our inputs are used as keys in the 
        self.key_fn = key_fn
        self.build() 

    def build(self):
        '''
        For every internal node, starting at the last one and ending at the root, we bubble it down
        to its correct position until the heap invariant is achieved
        This function is reused in the maximize function
        '''
        self.map = defaultdict(set)
        
        # for i in range(self.size):
        #     self.map[self.key_fn(self.heap[i])].add(i)    
        for i, node in enumerate(self.heap):
            self.map[self.key_fn(node)].add(i)
            
        inner_nodes = self.size // 2 
        for inner_node_index in range(inner_nodes-1, -1, -1):
            self.bubble_down(inner_node_index)      
            
    def bubble_down(self, p):
        '''
        Restore heap invariant by moving an element at index i down in the array 
        '''
        l = 2*p + 1
        r = l + 1
        min_index = p
        
        if l < self.size and (self.heap[l] < self.heap[min_index]):
            min_index = l
        if r < self.size and (self.heap[r] < self.heap[min_index]):
            min_index = r
            
        if min_index != p:
            self.swap(p, min_index)
            self.bubble_down(min_index)
              
    def bubble_up(self, i):
        '''
        Restore heap invariant by moving an element at index i up in the array 
        '''
        p = (i - 1) // 2
        if p >= 0 and (self.heap[p] > self.heap[i]):
            self.swap(p, i)
            self.bubble_up(p)
            
    def swap(self, i, j):
        '''
        Swap two elements in array and map
        '''
        self.map[self.key_fn(self.heap[i])].remove(i)
        self.map[self.key_fn(self.heap[j])].add(i)
        self.map[self.key_fn(self.heap[j])].remove(j)
        self.map[self.key_fn(self.heap[i])].add(j)
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
             
    def contains(self, element):
        return self.map[self.key_fn(element)]
    
            
    def add(self, element):
        '''
        Add an element to the end of the heap array and bubble it up
        '''
        self.heap.append(element)
        self.map[self.key_fn(element)].add(self.size)
        self.bubble_up(self.size)
        self.size += 1    
    
    def remove(self, element):
        '''
        First find the element, swap it with the last element. Remove the last element.
        Then fix the displaced element's position in the heap
        '''
        if self.contains(element):
            i = next(iter(self.map[self.key_fn(element)]))
            last = self.size - 1
            self.swap(i, last)
            self.heap.pop()
            self.map[self.key_fn(element)].remove(last)
            self.size -= 1
            
            self.heapify(i)
            
    def heapify(self, i):
        '''
        Given an index, it determines to bubble up or down to restore heap invariant
        Note that if element at index i is at the right spot, bubble_down and bubble_up functions just return
        '''
        p = (i - 1) // 2
        l = i * 2 + 1
        r = l + 1
        
        if p <= 0:
            self.bubble_down(i)
        elif self.heap[p] > self.heap[i]:
            self.bubble_up(i)
        else:
            self.bubble_down(i)
            
    def peek(self):
        return self.heap[0] if self.size > 0 else None
    
    def poll(self):
        if self.size == 0:
            return
        head = self.heap[0]
        self.remove(head)
        return head
    
    def isEmpty(self):
        return self.size == 0
    
    def debug_print(self):
        print('heap: ', end='')
        pprint(self.heap)
        print('map: ', end='')
        pprint(self.map)
           
    def maximize(self):
        '''
        Convert the min heap into a max heap by negating all the elements
        This works because the smallest element in the heap becomes the larget element after negation 
        '''
        self.heap = [-node for node in self.heap]
        self.build()
        self.heap = [-node for node in self.heap]
        self.map = defaultdict(set, {-element:self.map[self.key_fn(element)] for element in self.map})
        
    def __len__(self):
        return self.size
    
    def __bool__(self):
        return not self.isEmpty()


if __name__ == '__main__': 
    # h = MinHeap([1, 3, 9, 8, 3, 5, 7, 3, 7])
    
    tasks = [
        (5, 'shower'),
        (4, 'shave'),
        (1, 'cook'),
        (3, 'clean'),
        (6, 'study'),
        (0, 'shop'),
        (2, 'eat')
    ]
    
    taskQueue = MinHeap(tasks)
    taskQueue.debug_print()
    
