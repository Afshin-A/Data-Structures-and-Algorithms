from Tree.Node import Node

class AVLTree:
    def __init__(self):
        self._size = 0
        self._head: Node = None

    def add(self, value):
        # we never allow the abs(balance factor) of a node exceed
        # as soon as that happens, we balance the node using tree rotations
        
        def insert(root, value):
            pass
        


        if value == None:
            return False
        # no duplicates allowed
        if not self.contains(value):
            root = insert(root, value)
            self._size += 1
            return True
        else:
            return False
        
        

    def find(self, value) -> Node:
        current = self._head
        find_me = Node(value)
        while current and current != find_me:
            if  find_me < current:
                current = current.left
            elif find_me > current:
                current = current.right
        return current

    def contains(self, value) -> bool:
        return bool(self.find(value))

    def remove(self, node: Node):
        pass

    def calculate_height(self, node: Node):
        '''
        Height of a binary tree is the number of edges in the path from the root to the furthest leaf node. 
        That node will have a height of 0.
        To make that possible, the base case where a node height is 0 will return -1
        '''
        if node is None:
            return -1
        else:
            return 1 + max(self.calculate_height(node.left), self.calculate_height(node.right))
    
    def rotate_right(A: Node):
        '''
              P              P
             /              / 
            A              B
           / \            / \
          B   E          C   A      
         / \                / \
        C   D              D   E  
        Rotate around the node A, and return the node that takes its place
        This is important because if there's a parent to node A, then it must point
        to the successor of A, which is B. We can use the return value to set the child of P
        '''
        P = A.parent
        B = A.left
        D = B.right

        B.right = A
        A.parent = B

        A.left = D
        if D != None:
            D.parent = A
        
        B.parent = P
        if P.left == A:
            P.left = B
        else:
            P.right = B
            
        return B
    
    def rotate_left(A: Node):
        P = A.parent
        B = A.right
        D = B.left
        
        B.left = A
        A.parent = B

        A.right = D
        if D != None:
            D.parent = A
        
        B.parent = P
        if P.left == A:
            P.left = B
        else:
            P.right = B
            
        return B