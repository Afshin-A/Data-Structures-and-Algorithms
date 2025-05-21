from HashTable.HashMap import HashMap

'''

map from element to index
index = {
    A: 1,
    B: 2,
    C: 3,
}

parentIndex = []
size = []


'''

class UnionFind:
    def __init__(self, elements: list[int]):
        # map: element -> parent
        self.elements = elements
        # list tracks and stores all elements' parents
        self.parents = list(range(len(elements)))
        self.ranks = [0 for _ in elements]
    
        print(self.parents)
            
    def find(self, current_index):
        '''
        given the index of an element, returns the index of the root parent of that element
        '''
        if self.parents[current_index] != current_index:
            self.parents[current_index] = self.find(self.parents[current_index])  # path compression
        return self.parents[current_index]
       
    def _add(self, a, b):
        '''
        Given two indices of two elements, merges the two trees disjoint sets together
        This method performs path compression by adding to one tree to the root of the other tree, but it is not enough
        by itself. The find method does full path compression
        '''
        # index of root of a
        root_a = self.find(a)
        # index of root of b
        root_b = self.find(b)
        
        # if two roots are equal, that means they are already in the same group
        if root_a == root_b:
            return
        
        rank_a = self.ranks[root_a]
        rank_b = self.ranks[root_b]
        
        # add smaller tree to larger tree
        if rank_a > rank_b:
            # if a is a larger tree, a becomes parent of b
            self.parents[root_b] = root_a
        elif rank_a < rank_b:
            # if a is a smaller tree, b becomes parent of a
            self.parents[root_a] = root_b
        else:
            # if both trees have equal depth
            # add second tree to the first
            # i.e a becomes parent of b
            # depth of a increases by 1
            self.parents[root_b] = root_a
            self.ranks[root_a] += 1
    
    def add(self, a, b):
        '''
        This method allows adding via elements instead of indices of elements
        '''
        # this can be optamized using a hashmap for instant element loop up
        self._add(
            self.elements.index(a),
            self.elements.index(b)
        )
        
    def groups(self):
        '''Visualize the groups (disjoint sets) in the data structure'''
        groups = {}
        for i, val in enumerate(self.parents):
            if val not in groups:
                groups[val] = []
            groups[val].append(i)
        return list(groups.values())
            
    
    def __str__(self):
        return f'{self.parents}\n{self.ranks}'
    