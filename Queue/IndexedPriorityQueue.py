from Heap.MinHeap import MinHeap

# (priority, task)



class IndexedPriorityQueue:
    '''
    NOTE: There should be no duplicates tasks. It doesn't make sense for one task to have two priorities
    The MinHeap allows duplicates. Duplicates can be introduced by the queue arg in constructor. 
    '''
    def __init__(self, queue: list[tuple[int, str]]=[]):
        self.minHeap = MinHeap(queue, lambda x: x[1])
        # references
        # [(priority, object)]
        self.heap = self.minHeap.heap
        # map: object -> index in heap
        self.map = self.minHeap.map 
        
    def size(self):
        return len(self.minHeap)
    
    def isEmpty(self):
        return self.size() == 0  
    
    def enqueue(self, object: tuple[int, str]):
        if object in self.map:
            self.update_priority(object[1], object[0])
        else:
            self.minHeap.add(object)
    
    def dequeue(self):
        return None if self.isEmpty() else self.minHeap.poll()
    
    def update_priority(self, object, new_priority):
        if object in self.map:
            i = next(iter(self.map[object]))
            
            # tuples cannot be modified, so we create a new tuple with the new priority
            self.heap[i] = (new_priority, object)
            self.minHeap.heapify(i)
        else:
            self.enqueue((new_priority, object))
    
    def debug_print(self):
        #TODO: remove this
        print('heap status')
        self.minHeap.debug_print()
        
    def __contains__(self, task):
        return task in self.map
    
    def peek(self):
        return None if self.isEmpty() else self.minHeap.peek()
    
    def __len__(self):
        return self.size()
        
