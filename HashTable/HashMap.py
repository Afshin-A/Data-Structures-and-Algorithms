from abc import ABC, abstractmethod
from PrimeAlgorithms import find_next_prime, next_power_of_2
from HashTable.HashTable import Tombstone


class HashMapIterator:
    def __init__(self, keys, values):
        self.keys = keys
        self.values = values
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.keys):
            if self.keys[self.index] != None and not isinstance(self.keys[self.index], Tombstone):
                self.index += 1
                return self.keys[self.index], self.values[self.index]
            self.index += 1
        raise StopIteration
        

class HashMapInterface(ABC):
    def __init__(self, capacity=3, maxLoadFactor=0.75):
        if maxLoadFactor >= 1:
            raise ValueError('loadfactor greater than or equal to 1 will cause an infinite loop')
        self._capacity = capacity
        self._maxLoadFactor = maxLoadFactor
        self._threshold = int(capacity * maxLoadFactor)
        self._size = 0
        self._keys = [None] * self._capacity
        self._values = [None] * self._capacity
        self._TOMBSTONE = Tombstone()
        
    def size(self):
        return self._size    
       
    def hashCode(self, entry):
        return hash(entry) % self._capacity
    
    @abstractmethod
    def p(self, x, entry):
        pass
    
    @abstractmethod
    def _get_new_capacity(self):
        pass 
    
    def _resize_table(self):
        self._get_new_capacity()
        self._threshold = int(self._capacity * self._maxLoadFactor)
        self._size = 0
        keys_cache = self._keys.copy()
        values_cache = self._values.copy()
        self._keys = [None] * self._capacity 
        self._values = [None] * self._capacity
        print(self._capacity)
        for key, value in zip(keys_cache, values_cache):
            # print(i)
            if key and key != self._TOMBSTONE:
                self.add(key, value)
    
    def add(self, key, value):
        if key is None:
            raise ValueError('Key cannot be None')
        
        self._size += 1
        if self._size > self._threshold:
            self._resize_table()
            self._size += 1
        i = self.hashCode(key)
        x = 1
        while self._keys[i] != None:
            # If key exists, update value
            if self._keys[i] == key:
                break
            else:
                i = (i + self.p(x, key)) % self._capacity
                x += 1
        self._keys[i] = key
        self._values[i] = value
            
    def find(self, key):
        i = self.hashCode(key)
        first_tombstone_index = -1
        x = 0
        while self._keys[i] != None:
            if self._keys[i] is self._TOMBSTONE and first_tombstone_index == -1:
                first_tombstone_index = i
            elif self._keys[i] == key:
                if first_tombstone_index != -1:
                    self._keys[i], self._keys[first_tombstone_index] = self._keys[first_tombstone_index], self._keys[i]
                    self._values[i], self._values[first_tombstone_index] = self._values[first_tombstone_index], self._values[i]
                    self._keys[i] = None
                    self._values[i] = None
                    return first_tombstone_index
                else:
                    return i
            else:
                i = (i + self.p(x, key)) % self._capacity
                x += 1
        
        return -1
    
    def contains(self, key):
        return self.find(key) != -1
    
    
    def remove(self, key):
        index_to_remove = self.find(key)
        if index_to_remove != -1:
            self._keys[index_to_remove] = self._TOMBSTONE
            self._values[index_to_remove] = None
    
    def __str__(self):
        lines = []
        lines.append('index\tbucket\n')
        for i in range(self._capacity):
            lines.append(f'{i}\t{str(self._keys[i])}\t{str(self._values[i])}\n')
        return ''.join(lines)
    
    def __contains__(self, key):
        return self.contains(key)
    
    def __getitem__(self, key):
        return self._values[self.find(key)]
    
    def __setitem__(self, key, value):
        self.add(key, value)
    
    # generator  
    def __iter__(self):
        for i in range(self._capacity):
            if self._keys[i] is not None and self._keys[i] != self._TOMBSTONE:
                yield (self._keys[i], self._values[i])
    
    # iterator design pattern
    # def __iter__(self):
    #     return HashMapIterator(self._)
    

class HashMap(HashMapInterface):
    '''
    Linear probing
    '''  
    def p(self, x, entry):
        return x
    
    def _get_new_capacity(self):
        self._capacity = find_next_prime(self._capacity * 2)


class HashMapQuadratic(HashMapInterface):
    def p(self, x, entry):
        return x*(x+1)//2
    
    def _get_new_capacity(self):
        self._capacity = next_power_of_2(self._capacity * 2)


class HashMapDoubleHash(HashMapInterface):
    def _hash2(self, num):
        return 1 + (num % (self._capacity - 1))
    
    def p(self, x, entry):
        delta = max(self._hash2(entry) % self._size, 1)
        return (x*delta) % self._size
    
    def _get_new_capacity(self):
        self._capacity = find_next_prime(self._capacity * 2)
        