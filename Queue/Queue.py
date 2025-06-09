from LinkedList.DoublyLinkedList import DoublyLinkedList

class Queue:
    '''Representation of a queue data structure using a doubly-linked list.\n
    A queue is similar to a line. Elements are added at the end, and they are removed from the begining of the list.\n
    First in last out
    '''
    def __init__(self):
        self._queue = DoublyLinkedList()
        self._size = self._queue.size()
        
    def size(self):
        return self._queue.size()
    
    def isEmpty(self):
        return self.size() == 0
    
    def enqueue(self, data):
        '''Adds a node to the bottom of the list\n
        This is sometimes called offer\n
        O(1)
        '''
        self._queue.addLast(data)
        
    def add(self, data):
        self.enqueue(data)
    
    
    def dequeue(self):
        '''Removes and returns the node at the top of the list\n
        This is sometimes called polling\n
        O(1)
        '''
        return self._queue.removeFirst()
    
    def poll(self):
        return self.dequeue()
    
    def peek(self):
        '''Returns the data of the top most node\n
        O(1)
        '''
        return self._queue.peekFirst()
    
    def contains(self, data):
        return self._queue.contains(data)
    
    def remove(self, data):
        '''Removes the first most node that matches the given data\n
        O(n)
        '''
        return self._queue.remove(data)
    
    
# we can use a static array of fixed size if we know the maximum number of elements in our queue
class ArrayQueue:
    '''
    This class uses a static array to implement the queue data structure\n
    The queue has a fixed size. Adding enqueuing elements when the queue is full causes an error\n
    We use modular arithmetic to dynamically calculate the indices for head and tail of the stack. This way, we don't need to 
    move elements around, and enqueue and dequeue will have O(1) time complexities. 
    '''
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._queue = [None] * capacity
        self._size = 0
        self._front = self._rear = 0
        
    def isFull(self):
        return self._size >= self._capacity
    
    def isEmpty(self):
        return self._size == 0
    
    def peek(self):
        return self._queue[self._rear]
    
    def enqueue(self, data):
        if self.isFull():
            raise RuntimeError('Queue is alreaddy full. Cannot add more elements at this time')
        self._rear = (self._size + self._front) % self._capacity
        self._queue[self._rear] = data
        self._size += 1
        
        
    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError('Queue is empty. Cannot dequeue')
        
        dequeue_value = self._queue[self._front]
        self._queue[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return dequeue_value
    
    def __str__(self):
        string = ''
        for element in self._queue:
            string += f'{element}\t'
        return string
    
    def __getitem__(self, index):
        if index >= self._capacity:
            raise IndexError('Invalid index')
        return self._queue[(self._front + index) % self._capacity]