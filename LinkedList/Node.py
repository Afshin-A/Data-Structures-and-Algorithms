class Node:
    def __init__(self, data=None):
        self.next: Node = None
        self.prev: Node = None
        self.data: any = data
        
    def __str__(self):
        return f'{self.data}'