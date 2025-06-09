from HashTable.HashMap import HashMap
from deprecated import deprecated




@deprecated(reason="This implementation was too complicated. Please use the UnionFind class found in the UnionFindIndex module instead.")
class UnionFind:
    def __init__(self, elements: list[int]):
        # map: element -> parent
        self.elements = elements
        self.indices = HashMap()
        self.parents = HashMap()
        self.ranks = HashMap()
        
        # at first, every element is its own parent
        for parent, element in enumerate(elements):
            self.indices.add(element, parent)
            self.parents.add(element, parent)
            self.ranks.add(element, 0)
            
    def find(self, element):
        '''
        Finds and returns the root of the given element
        Performs path compression
        '''
        parent_index = self.parents[element]
        parent = self.elements[parent_index]
        # if the element's parent is itself, we've found the root
        if element == parent:
            return element
        else:
            return self.find(parent)
        
    def add(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        # print(f'adding {a} and {b}')
        # print(f'roof of {a}: {root_a}')
        # print(f'roof of {b}: {root_b}')
        
        # if roots are equal, that means a and b are already in the same group
        if root_a == root_b:
            return
        
        rank_a = self.ranks[root_a]
        rank_b = self.ranks[root_b]
        
        # add smaller tree to larger tree
        if rank_a > rank_b:
            # if a is a larger tree, a becomes parent of b
            self.parents[root_b] = self.indices[root_a]
        elif rank_a < rank_b:
            # if a is a smaller tree, b becomes parent of a
            self.parents[root_a] = self.indices[root_b]
        else:
            # if both trees have equal depth
            # add second tree to the first
            # i.e a becomes parent of b
            # depth of a increases by 1
            self.parents[b] = self.indices[root_a]
            self.ranks[root_a] += 1
    
    def __str__(self):
        parents = []
        ranks = []
        for element in self.elements:
            parents.append(self.elements[self.parents[element]])
            ranks.append(self.ranks[element])
        return f'E\t{self.elements}\nP\t{parents}\nR\t{ranks}'
    