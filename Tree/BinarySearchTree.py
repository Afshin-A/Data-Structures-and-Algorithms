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
    
    def find(self, data):
        pass
    
    def remove(self, data):
        pass
        
        
    def dispay1(self, current: Node):
        if not current:
            return
        print(current, end=' ')
        self.dispay(current.left)
        self.dispay(current.right)
    
    def dispay2(self, current: Node):
        if not current:
            return
        self.dispay2(current.left)
        print(current, end=' ')
        self.dispay2(current.right)

    def dispay3(self, current: Node):
        if not current:
            return
        self.dispay3(current.left)
        self.dispay3(current.right)
        print(current, end=' ')