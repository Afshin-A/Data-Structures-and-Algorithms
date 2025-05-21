from time import sleep
from LinkedList.Node import Node

class DoublyLinkedList:
    def __init__(self):
        self._head:Node
        self._tail:Node
        self._head = self._tail = None
        self._size:int = 0
    
    def isEmpty(self):
        '''
        Utility method, checks if the list is empty \n
        O(1)
        '''
        return self._size == 0
    
    def size(self):
        '''
        Utility method, returns the number of nodes in the list \n
        O(1)
        '''
        return self._size
    
    def __str__(self):
        '''
        Returns a string visualization of the list \n
        O(n)
        '''
        string = ''
        head = self._head
        while head is not self._tail:
            string += f'{head}→'
            head = head.next
        string += str(self._tail)
        return string
    
    def traverseBack(self):
        '''
        Testing method to ensure we can move backwards \n
        O(n)
        '''
        string = ''
        tail = self._tail
        while tail:
            print(f'current node: {tail.data}')
            string += str(tail)
            tail = tail.prev
        print('exiting traverseBack')
        return string
    
    
    def clear(self):
        '''
        Goes through each node in the list and deletes it \n
        O(n)
        '''
        while self._head:
            # get a pointer to head
            head = self._head
            # detatch current node from the list
            head.prev = head.next = None
            # remove node data
            head.data = None
            # reduce list size
            self._size -= 1
            # move up to the next node
            self._head = self._head.next
            
        # head should be None
        self._head = self._tail = None
        
    def addFirst(self, data):
        '''
        Creates and prepends a node to the list \n
        O(1)
        '''
        node = Node(data)
        if self.isEmpty():
            self._head = self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
        self._size += 1
        
    def addLast(self, data):
        '''
        Creates and appends a node to the list \n
        O(1)
        '''
        node = Node(data)
        if self.isEmpty():
            self._head = self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node
        self._size += 1
        
    
    def peekFirst(self):
        '''
        Peeks at the first node in the list
        '''
        if self.isEmpty():
            raise RuntimeError('List is empty.')
        return self._head.data
    
    def peekLast(self):
        '''Peeks at the last node in the list
        '''
        if self.isEmpty():
            raise RuntimeError('List is empty.')
        return self._tail.data
    
    def removeFirst(self):
        '''Removes the first element from the list and returns its data\n
        O(1)
        '''
        if self.isEmpty():
            raise RuntimeError('List is empty. Nothing to remove.')
        
        data = self._head.data
        
        # move up the head
        self._head = self._head.next
        # reduce the size
        self._size -= 1
        
        # was there only 1 element in list? is list now empty?
        if self.isEmpty():
            # if so, head is now None
            # set the tail to None
            self._tail = None
            # no references to previous node, garbage collection will remove it
        else:
            # we need to remove the previous node
            self._head.prev = None                        
            # no references to previous node, garbage collection will remove it

        return data
        
        '''
        if self._head == self._tail:
            self._head = self._tail = None
        else:
            # move the head up by 1 node
            self._head = self._head.next
            # remove the reference to the previous node
            self._head.prev = None
            # because nothing references the previous node, it is now eilgible for automatic garbage collection
        self._size -=1
        '''
        
    def removeLast(self):
        '''Removes the last node from the list and returns its data \n
        O(1)
        '''
        if self.isEmpty():
            raise RuntimeError('List is empty. Nothing to remove.')
        # store the data to return later
        data = self._tail.data
        # go back to the previous node
        self._tail = self._tail.prev
        # lower the size
        self._size -= 1
        
        # if the list is empty, the tail should be None
        if self.isEmpty():
            # set the head to None as well
            self._head = None
            # with no pointers to the previous node, python garbage collection will automatically remove it
        else:
            # list is not empty, so remove the pointer to the previous tail
            # python auto garbage collection will remove it
            self._tail.next = None
            
        return data
    
    
    def removeNode(self, node: Node):
        '''Removes a specific node given its pointer\n
        O(1)
        '''
        if node == self._head:
            return self.removeFirst()
        elif node == self._tail:
            return self.removeLast()
        else:
            # node is in the middle of the list
            data = node.data
            prev = node.prev
            next = node.next
                
            prev.next = next
            next.prev = prev
            return data
        

    def removeAt(self, index: int):
        '''Remove node at a specific index \n
        O(n/2) → O(n)
        '''
        if type(index) is not int:
            raise TypeError('Index must be an integer.')
        if index < 0 or index >= self._size:
            raise IndexError('Index out of bounds.')
        if index <= self._size / 2:
            # search from the head
            remove_me = self._head
            for i in range(index):
                remove_me = remove_me.next
        else:
            remove_me = self._tail
            for i in range(self._size - 1 - index):
                remove_me = remove_me.prev
                
        return self.removeNode(remove_me)
    
    def indexOf(self, data):
        '''Returns index of node which contains the given data \n
        O(n)
        '''
        current_node = self._head
        for index in range(self._size):
            if current_node.data == data:
                return index
            current_node = current_node.next
        return -1
            
    def contains(self, data):
        '''Returns wether any node with the given data exists \n
        O(n)
        '''
        return self.indexOf(data) != -1
    
    def remove(self, data):
        '''First finds the index of the first node with the given data, then removes that node from the list\n
        O(n)
        '''
        return self.removeAt(
            self.indexOf(data)
        )


    def __iter__(self):
        return DoublyLinkedListIterator(self._head)
    
    
    
class DoublyLinkedListIterator:
    def __init__(self, start_node):
        self.current = start_node
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next
        return data