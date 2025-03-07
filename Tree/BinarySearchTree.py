from Tree.Node import Node

class BST:
    def __init__(self):
        self._size = 0
        self._head = None
        
    def add(self, data):
        '''
        Worst case time complexity: O(n)
        Average time complexity: O(log(n))
        Inserts an element to the binary search tree
        '''
        node = Node(data)
        if self._head is None:
            self._head = node
            self._size += 1
            return
        
        current = self._head
        
        while True:
            if current:
                if node < current:
                    if current.left:
                        current = current.left
                    else:
                        current.left = node
                        break
                elif node > current:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node
                        break
                else:
                    return
        
        self._size += 1
            
    def add2(self, data):
        '''
        A more readable/factored version of the add method
        '''
        node = Node(data)
        if self._head is None:
            self._head = node
            self._size += 1
            return
        
        current = self._head
        while current:
            parent = current
            if node < current:
                current = current.left
            elif node > current:
                current = current.right
            else:
                return
        
        if node < parent:
            parent.left = node
        else:
            parent.right = node
        
        self._size += 1
        return
    
    def find(self, data) -> Node:
        current = self._head
        find_me = Node(data)
        while current and current != find_me:
            if  find_me < current:
                current = current.left
            elif find_me > current:
                current = current.right
        return current

    def contains(self, data) -> bool:
        return bool(self.find(data))

    def remove(self, data):
        remove_me = self.find(data)
        if not remove_me:
            return
        if not (remove_me.left and remove_me.right):
            remove_me = None

    def display1(self):
        self._display1(self._head)

    def display2(self):
        self._display2(self._head)
    
    def display3(self):
        self._display3(self._head)
    
        
    def _display1(self, current: Node):
        if not current:
            return
        print(current, end=' ')
        self._display(current.left)
        self._display(current.right)
    
    def _display2(self, current: Node):
        if not current:
            return
        self._display2(current.left)
        print(current, end=' ')
        self._display2(current.right)

    def _display3(self, current: Node):
        if not current:
            return
        self._display3(current.left)
        self._display3(current.right)
        print(current, end=' ')
    
