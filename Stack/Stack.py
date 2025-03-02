from LinkedList.DoublyLinkedList import DoublyLinkedList

class Stack:
    def __init__(self):
        self._stack = DoublyLinkedList()
        self._size = self._stack._size
        
    def push(self, data):
        self._stack.addLast(data)
        
    def pop(self):
        return self._stack.removeLast()
    
    def peek(self):
        return self._stack.peekLast()
    
    def size(self):
        return self._size
    
    def isEmpty(self):
        return self._stack.isEmpty()
    

    
    
