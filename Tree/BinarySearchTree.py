from Tree.Node import Node
from Queue.Queue import Queue
from deprecated import deprecated
from Stack.Stack import Stack

class BST:
    def __init__(self):
        self._size = 0
        self._head = None

    @deprecated('Use add2 instead')    
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
                # data already exists in table
                # exit because no duplicates allowed in our implementation
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
        '''
        
        '''
        # instead of keeping track of the parent and if we're the left or right child of the parent,
        # we recursively just set the child of that parent
        def remove(root: Node, data):
            '''
            Given some data and a root node, it recursively searches for a node with the same data starting at the given root node
            Returns successor 
            '''
            # First we need to find the node with the given data

            # if we hit an null node, node doesn't exist and return None
            if root == None:
                return None
            if data < root.data:
                root.left = remove(root.left, data)
            elif data > root.data:
                root.right = remove(root.right, data)
            # Node found
            else:
                # no need to check if node is a leaf node because case 1 covers it

                # case 1: no left child. right child becomes successor
                if root.left is None:
                    return root.right
                # case 2: no right child. left child becomes successor
                if root.right is None:
                    return root.left
                    
                # case 3: both children exist. two possible successors
                # largest element in the left subtree or
                # smallest element in the right subtree

                successor = root.right
                while successor.left is not None:
                    successor = successor.left

                root.data = successor.data
                # delete the successor, which is a leaf node
                # no need to start searching for the successor from the head node
                # we search for it starting at the root of that subtree
                # this assumes there are no duplicate values in the tree
                # if the tree allowed duplicate values, we would instead have to identify nodes by pointers/references
                root.right = remove(root.right, successor.data)
            return root

        return remove(self._head, data)

    def preorder(self):
        '''
        Returns a list of tree elements in a preorder manner
        '''
        results = []
        def _preorder(current: Node):
            if not current:
                return
            results.append(current)
            _preorder(current.left)
            _preorder(current.right)

        _preorder(self._head)
        return results

    def inorder(self):
        results = []
        def _inorder(current: Node):
            if not current:
                return
            _inorder(current.left)
            results.append(current)
            _inorder(current.right)
        
        _inorder(self._head)
        return results
    
    def postorder(self):
        results = []
        def _postorder(current: Node):
            if not current:
                return
            _postorder(current.left)
            _postorder(current.right)
            results.append(current)

        _postorder(self._head)
        return results

    def breadthFirst(self):
        queue = Queue()
        results = []
        if self._head is None:
            return
        queue.enqueue(self._head)
        while not queue.isEmpty():
            n = queue.poll()
            results.append(n)
            if n.left:
                queue.enqueue(n.left)
            if n.right:
                queue.enqueue(n.right)
        return results
    
    def depthFirst(self):
        stack = Stack()
        visited = []
        leaf_nodes = []

        stack.push(self._head)

        while not stack.isEmpty():
            current_visited: Node = stack.pop()
            visited.append(current_visited)

            if current_visited.right:
                stack.push(current_visited.right)
            if current_visited.left:
                stack.push(current_visited.left)
            if not (current_visited.left or current_visited.right):
                leaf_nodes.append(current_visited)

        return visited, leaf_nodes


    def height(self, root:Node=None):
        def height(root):
            if root is None:
                return -1
            else:
                return 1 + max(height(root.left), height(root.right))
            
        if root == None:
            root = self._head
        return height(root)
    
    def to_array_complete_tree(self):
        height = self.height()
        total = 2 ** height - 1
        tree = [None] * total
        root = self._head
        parent = 0
        left = 2*parent + 1
        right = left + 1
        queue = Queue()
        results = []
        
        queue.enqueue(root)
        while not queue.isEmpty():
            n = queue.poll()
            results.append(n)
            if n.left:
                queue.enqueue(n.left)
            if n.right:
                queue.enqueue(n.right)
    