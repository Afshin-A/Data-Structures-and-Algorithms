from LinkedList.DoublyLinkedList import DoublyLinkedList
from PrimeAlgorithms import find_next_prime, is_prime

class HashtableSeperateChaining:
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

                
        

    
class HashTableLinearProbing:
    '''
    if a collision occurs, we use a probing function to find the next index
    to insert an entry into the hashtable. 
    there can be many probing functions, such as linear, quadratic, double hashing, 
    and even using pseudo random numbers. 
    whatever function we use, we must ensure that an infinite loop doesn't occur
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
        # starting table size
        self._capacity = capacity
        # percentage of all elements in the hashtable. higher percentage means the table is crowded and find/add/remove become less optimized
        # if maxLoadFactor is 2, for example, we resize the table if size is more than twice the capacity
        self._maxLoadFactor = maxLoadFactor
        self._threshold = int(capacity * maxLoadFactor)
        # number of elements currently in the hashtable
        self._size = 0
        self._table: list[int] = [None] * self._capacity
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
        
        # add logic for adding to table
        x = 0
        index = self.hashCode(entry)
        while self._table[index] != None:
            index = (index + self.p(x)) % self._capacity
            x += 1
        self._table[index] = entry
           
    
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
        match self._probing_method:
            case 'linear':
                pass
            case 'quadratic:':
                pass
            case 'double_hashing':
                pass
                    
    def __str__(self):
        string = 'index\tbucket\n'
        for i in range(self._capacity):
            string += f'{i}\t{str(self._table[i])}\n'
        return string
    
    def p(self, x, entry=None):
        '''
        Probing function that depends on the user's choice of probing method
        '''
        match self._probing_method:
            case 'linear':
                # return ax where gcd(a, self._size)=1
                # in other words, a and table size need to be coprimes to avoid an infinite loop 
                return x
            case 'quadratic':
                # table size must be a power of 2
                return (x**2 + x)/2
            case 'double_hash:':
                # table size must be prime
                delta = hash2(entry) % self._size
                if delta == 0:
                    delta += 1
            
                pass
            case _:
                pass