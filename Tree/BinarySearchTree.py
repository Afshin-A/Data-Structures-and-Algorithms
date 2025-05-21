from Tree.Node import Node
from Queue.Queue import ArrayQueue

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
            if current != None:
                if node < current:
                    if current.left != None:
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
        while current != None:
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
        pass
    
    def remove(self, data):
        pass
        
        
    def preorder_traversal(self) -> list:
        nodes = []
        def traverse(current: Node):
            if current == None:
                return
            nodes.append(current.data)
            traverse(current.left)
            traverse(current.right)
            
        traverse(self._head)
        return nodes
    
    def inorder_traversal(self):
        nodes = []
        def traverse(current: Node):
            if current == None:
                return
            traverse(current.left)
            nodes.append(current.data)
            traverse(current.right)
            
        traverse(self._head)
        return nodes

    def postorder_traversal(self):
        nodes = []
        def traverse(current: Node):
            if current == None:
                return
            traverse(current.left)
            traverse(current.right)
            nodes.append(current.data)
            
        traverse(self._head)
        return nodes
    
    def breath_first_traversal(self):
        nodes = []
        if self._head == None:
            return nodes
        
        node_visit_order = ArrayQueue(self._size)
        node_visit_order.enqueue(self._head)
        while not node_visit_order.isEmpty():
            current = node_visit_order.dequeue()
            nodes.append(current)
            if current.left:
                node_visit_order.enqueue(current.left)
            if current.right:
                node_visit_order.enqueue(current.right)
                    
        return nodes
    
    def isSymmetric(self) -> bool:
        '''
        In essense, we're doing a breadth first search of pairs of nodes. Each node is paired with its mirror node
        
        if n1 == none and n2 == none:
            continue

        # if we reached here, that means both n1 and n2 are not none
        # this means that n1 might be none
        # this means that n2 might be none
        # this means that both could be none

        if n1 == none or n2 == none:
            # if at least one of the above statements are true, we return false
            return false

        # if we reached here, that means that:
        # both n1 and n2 are not none
        # one of them is not none either
        # so we conclude that neither is none
        '''
        
        if self._head == None:
            return True
        
        symmetric_pairs = ArrayQueue(self._size)
        symmetric_pairs.enqueue((self._head.left, self._head.right))
        while not symmetric_pairs.isEmpty():
            n1, n2 = symmetric_pairs.dequeue()
            # if both nodes are none, we contrinue
            if n1 == None and n2 == None:
                continue
            # if exactly one node is none, tree cannot be symmetric 
            # we can also use or instead of xor
            if (n1 == None) ^ (n2 == None):
                return False
            # since both nodes are not none, and one is not none either, we can conclude both are not none
            # therefore, we check for their values
            if n1.data != n2.data:
                return False
            # just like a breadth first search, we add more pairs of nodes to the queue
            symmetric_pairs.enqueue((n1.left, n2.right))
            symmetric_pairs.enqueue((n1.right, n2.left))
            
        return True
    
    
    