from LinkedList.DoublyLinkedList import DoublyLinkedList
from PrimeAlgorithms import find_next_prime, next_power_of_2
from warnings import warn


class Tombstone:
    '''
    Dummy class signifies when an index in a hashtable was previously occupied but now deleted
    '''
    def __str__(self):
        return 'T'

class HashTableSeperateChaining:
    '''
    Open chaining implementation of hash table
    '''
    def __init__(self, capacity=3, maxLoadFactor=2, probing_method='linear'):
        # table size
        self._capacity = capacity
        # percentage of all elements in the hashtable. higher percentage means the table is crowded and find/add/remove become less optimized
        # if maxLoadFactor is 2, for example, we resize the table if size is more than twice the capacity
        self._maxLoadFactor = maxLoadFactor
        self._threshold = int(capacity * maxLoadFactor)
        # number of elements currently in the hashtable
        self._size = 0
        self._table: list[DoublyLinkedList] = [None] * self._capacity
        self._probing_method = probing_method
        
    def size(self):
        return self._size    
       
    def hashCode(self, entry):
        return hash(entry) % self._capacity
     
    # allows duplicates
    def add(self, entry):
        self._size += 1
        if self._size > self._threshold:
            self.resizeTable()
        
        index = self.hashCode(entry)
        if not self._table[index]:
            self._table[index] = DoublyLinkedList()
            
        self._table[index].addLast(entry)
           
    
    def remove(self, entry):
        index = self.hashCode(entry)
        bucket = self._table[index]
        if bucket:
            return bucket.remove(entry)
        return None
    
    
    def contains(self, entry):
        index = self.hashCode(entry)
        if self._table[index]:
            return self._table[index].contains(entry)
        else:
            return False
    
    def resizeTable(self):
        # print('Resizing table')
        # print('Current capacity: ', self._capacity)
        # print('Current size: ', self._size)
        
        # temporarily store these variables for later use in this function
        old_capacity = self._capacity
        old_table = self._table
        
        # update capacity
        self._capacity *= 2
        # update threshold
        self._threshold = int(self._capacity * self._maxLoadFactor)
        # update table
        self._table = [None] * self._capacity
        
        # for each item in each bucket in the old table, we find a new position in the new, resized table
        for i in range(old_capacity):
            bucket = old_table[i]
            if bucket:
                for element in bucket:
                    self.add(element)
                    
    def __str__(self):
        string = 'index\tbucket\n'
        for i in range(self._capacity):
            string += f'{i}\t{str(self._table[i])}\n'
        return string

    
class HashTable:
    '''
    Open addressing implementation of a hash table
    
    When a collision occurs, we use a probing function to find the next suitable index
    to insert an entry into the hashtable. 
    Supported probing functions: linear, quadratic, double_hash.
    TODO: Add pseudo random numbers. 
    Whatever function we use, we must ensure that an infinite loop doesn't occur
    '''
    '''
    x = 1
    index = hash(entry)
    while table[index] != null:
        index = (index + P(entry, x)) % capacity
        x += 1
    insert entry at table[index]
    
    '''
    def __init__(self, capacity=3, maxLoadFactor=0.75, probing_method='linear'):
        if maxLoadFactor >= 1:
            raise ValueError('loadfactor greater than or equal to 1 will cause an infinite loop')
        # Maximum table size allowed
        self._capacity = capacity
        # Percentage of all elements in the hashtable. Higher percentage means the table is crowded and find/add/remove become less optimized
        # Example: if maxLoadFactor == 2, we resize the table if size is more than twice the capacity. 
        self._maxLoadFactor = maxLoadFactor
        self._threshold = int(capacity * maxLoadFactor)
        # Number of elements currently in the hashtable
        self._size = 0
        self._table: list[int] = [None] * self._capacity
        self._probing_method = probing_method 
        
        # Marks where an element in the table was previously removed
        self._TOMBSTONE = Tombstone()    
     
    def size(self):
        return self._size 
       
    def hashCode(self, entry):
        '''
        Primary hashing used for linear and quadratic hashing
        '''
        return hash(entry) % self._capacity
    
    def _hash2(self, num):
        '''
        Secondary hashing used for double hashing
        '''
        return 1 + (num % (self._capacity - 1))
        
    def p(self, x, entry):
        '''
        Probing function based on the user's choice of probing method
        '''
        match self._probing_method:
            case 'linear':
                # Return a*x where gcd(a, self._size)=1. a and size must be co-primes. Thus, a=1
                # This can also be ensured if table size is prime
                return x
            case 'quadratic':
                # Table size must be a power of 2
                return (x**2 + x)//2
            case 'double_hash':
                # Table size must be prime                
                # Delta cannot be 0, or an infinite loop occurs when adding, because any number mod 0 is 0
                delta = max(self._hash2(entry) % self._size, 1)
                return (x*delta) % self._size
            case _:
                warn('Probing method is undefined. Setting to linear.')
                self._probing_method = 'linear'
                return self.p(x)
           
    def add(self, entry):
        '''
        Adds an element or a list of elements into the hashtable. Allows duplicates
        '''
        if isinstance(entry, (list, set, tuple)):
            for element in entry:
                self.add(element)
        else:
            self._size += 1
            if self._size > self._threshold:
                self._resizeTable()
                # _resizeTable sets the size to 0 and builds it from the ground up. This leads to ignoring the
                # size incrementation we do above. So we need to add it again
                self._size += 1
            
            i = self.hashCode(entry)
            x = 1
            while self._table[i] != None:
                # note: we need to pass along entry in case probing method is double_hash. it's not used for other probing  methods
                i = (i + self.p(x, entry)) % self._capacity
                x += 1
            self._table[i] = entry
        
    
    def remove(self, entry):
        '''
        Removes an element from the hashtable
        '''
        index_to_remove = self.find(entry)
        if index_to_remove == -1:
            return
        self._table[index_to_remove] = self._TOMBSTONE
        
    
    def find(self, entry):
        '''
        Finds and returns the index of the given element. Returns -1 if it doesn't exist
        '''
        i = self.hashCode(entry)
        first_tombstone_index = -1
        x = 0
        while self._table[i] != None:
            if self._table[i] is self._TOMBSTONE and first_tombstone_index == -1:
                # first index where it was previously removed
                first_tombstone_index = i
            elif self._table[i] == entry:
                if first_tombstone_index != -1:
                # performing search optimization by reducing number of probes needed to find this entry. 
                    self._table[i], self._table[first_tombstone_index] = self._table[first_tombstone_index], self._table[i]
                    self._table[i] = None
                    # Since we removed a Tombstone, we need to reduce the table size. Tombstones count towards the size,
                    # but they are not transfered over during resizing
                    self._size -= 1
                    return first_tombstone_index
                else:
                    return i
            else:
                # probe to next index
                i = (i + self.p(x, entry)) % self._capacity
                x += 1
        return -1
    
    def contains(self, entry):
        '''
        Returns wether the given element exists in the hashtable
        '''
        return self.find(entry) != -1
    
    def _resizeTable(self):
        '''
        Resizes the table when size surpasses the threshold
        '''
        match self._probing_method:
            case 'linear' | 'double_hash':
                self._capacity = find_next_prime(self._capacity * 2)
            case 'quadratic':
                self._capacity = next_power_of_2(self._capacity * 2)
            case _:
                warn('Probing method is undefined. Setting to linear.')
                self._probing_method = 'linear'
                self._capacity = find_next_prime(self._capacity * 2)
        
        # updating the threshold
        self._threshold = int(self._capacity * self._maxLoadFactor)
        
        table_cache = self._table.copy()
        # Because Tombstones count towards the size and we will not add them to the new table, we set the size to 0
        # and allow the add method to build the size up again
        self._size = 0
        self._table = [None] * self._capacity
        
        for element in table_cache:
            if element and element != self._TOMBSTONE:
                self.add(element)
                                
                    
    def __str__(self):
        # print('capacity:' , self._capacity)
        # print('size: ', self._size)
        
        lines = []
        lines.append('index\tbucket\n')
        for i in range(self._capacity):
            lines.append(f'{i}\t{str(self._table[i])}\n')
        return ''.join(lines)
    
    
    def __contains__(self, entry):
        return self.contains(entry)
    
    def __getitem__(self, index):
        return self._values[self.find(key)]
    
    def __setitem__(self, index, value):
        self.add(key, )
    
    # generator  
    def __iter__(self):
        for i in range(self._capacity):
            if self._keys[i] is not None and self._keys[i] != self._TOMBSTONE:
                yield (self._keys[i], self._values[i])
    