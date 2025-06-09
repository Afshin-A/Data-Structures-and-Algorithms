from abc import ABC, abstractmethod
from PrimeAlgorithms import find_next_prime, next_power_of_2
from HashTable.HashTable import Tombstone

class HashTableIterator:
    def __init__(self, table):
        self.table = table
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.table):
            if self.table[self.index] != None and not isinstance(self.table[self.index], Tombstone):
                self.index += 1
                return self.table[self.index]
            self.index += 1
        raise StopIteration

class HashTableInterface(ABC):
    def __iter__(self):
        return HashTableIterator(self._table)
    
    def __init__(self, capacity=3, maxLoadFactor=0.75):
        if maxLoadFactor >= 1:
            raise ValueError('loadfactor greater than or equal to 1 will cause an infinite loop')
        self._capacity = capacity
        self._maxLoadFactor = maxLoadFactor
        self._threshold = int(capacity * maxLoadFactor)
        self._size = 0
        self._table: list[int] = [None] * self._capacity
        self._TOMBSTONE = Tombstone()
    
    def size(self):
        return self._size    
       
    def hashCode(self, entry):
        return hash(entry) % self._capacity
    
    @abstractmethod
    def p(self, x, entry):
        pass
    
    @abstractmethod
    def _get_new_size(self):
        pass 
    
    def _resize_table(self):
        self._get_new_size()
        self._threshold = int(self._capacity * self._maxLoadFactor)
        table_cache = self._table.copy()
        # resetting table size
        self._size = 0
        self._table = [None] * self._capacity
        for element in table_cache:
            if element and element != self._TOMBSTONE:
                # incrementing table size for non Tombstone elements only
                self.add(element)
    
    def add(self, entry):
        if isinstance(entry, (list, set, tuple)):
            for element in entry:
                self.add(element)
        else:
            self._size += 1
            if self._size > self._threshold:
                self._resize_table()
                # _resizeTable sets the size to 0 and builds it from the ground up. This leads to ignoring the
                # size incrementation we do above. So we need to add it again
                self._size += 1
                
            i = self.hashCode(entry)
            x = 1
            while self._table[i] != None:
                i = (i + self.p(x, entry)) % self._capacity
                x += 1
            self._table[i] = entry
            
    def find(self, entry):
        i = self.hashCode(entry)
        first_tombstone_index = -1
        x = 0
        while self._table[i] != None:
            if self._table[i] is self._TOMBSTONE and first_tombstone_index == -1:
                first_tombstone_index = i
            elif self._table[i] == entry:
                if first_tombstone_index != -1:
                    self._table[i], self._table[first_tombstone_index] = self._table[first_tombstone_index], self._table[i]
                    self._table[i] = None
                    self._size -= 1
                    return first_tombstone_index
                else:
                    return i
            else:
                i = (i + self.p(x, entry)) % self._capacity
                x += 1
        return -1
    
    def contains(self, entry):
        return self.find(entry) != -1
    
    def remove(self, entry):
        index_to_remove = self.find(entry)
        if index_to_remove == -1:
            return
        self._table[index_to_remove] = self._TOMBSTONE
        # removing an element places Tombstone in its place, so size does not decreasae
        # self._size -= 1
    
    def __str__(self):
        lines = []
        lines.append('index\tbucket\n')
        for i in range(self._capacity):
            lines.append(f'{i}\t{str(self._table[i])}\n')
        return ''.join(lines)
    
    def __contains__(self, entry):
        '''
        Returns if entry is in the hashtable
        '''
        return self.contains(entry)
    
    
    
    def __getitem__(self, entry):
        '''
        Returns the index at which entry is stored in the internal database
        This doesn't have any applications besides providing a shorter syntax for the custom UnionFind data structure
        '''
        index = self.find(entry)
        return index if index != -1 else None
    
    
    

class HashTable(HashTableInterface):
    '''
    Hash table that uses linear probing to resolve collisions
    '''    
    def p(self, x, entry):
        return x
    
    def _get_new_size(self):
        self._capacity = find_next_prime(self._capacity * 2)


class HashTableQuadraticProbe(HashTableInterface):
    def p(self, x, entry):
        return x*(x+1)//2
    
    def _get_new_size(self):
        self._capacity = next_power_of_2(self._capacity * 2)


class HashTableDoubleHashProbe(HashTableInterface):
    def _hash2(self, num):
        return 1 + (num % (self._capacity - 1))
    
    def p(self, x, entry):
        delta = max(self._hash2(entry) % self._size, 1)
        return (x*delta) % self._size
    
    def _get_new_size(self):
        self._capacity = find_next_prime(self._capacity * 2)