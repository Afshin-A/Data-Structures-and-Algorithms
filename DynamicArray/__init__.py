class DynamicArray:
    def __init__(self, capacity=1):
        self._length = 0
        self._capacity = capacity
        self._array = self._make_array(self._capacity)
        
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, new_capacity):
        raise AttributeError('You can\'t change this property')
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, new_length):
        raise AttributeError('You can\'t change this property')
    
        
    def _make_array(self, capacity):
        """
        Helper function to create an array of given capacity
        """
        return [None] * capacity
        
    def __len__(self):
        return self._length
    
    def __getitem__(self, k):
        if not 0 <= k < self._length:
            raise IndexError('invalid index')
        return self._array[k]
    
    def append(self, obj):
        if self._length >= self._capacity:
            # increase capacity
            self._capacity = self._capacity * 2
            # create new array with new capacity
            new_array = self._make_array(self._capacity)
            # copy all the elements to the new array
            for index in range(self._length):
                new_array[index] = self._array[index]
            self._array = new_array
            
        # append the object to the end of the array
        self._array[self._length] = obj
        # increase length
        self._length += 1
        
        
    def __setitem__(self, k, obj):
        if not 0 <= k < self._length:
            raise IndexError('invalid index')
        self._array[k] = obj
        
    def __getitem__(self, k):
        if not 0 <= k < self._length:
            raise IndexError('invalid index')
        return self._array[k]
        
    def __str__(self):
        return str(self._array)
    
    def replace(self, old_obj, new_obj):
        for i in range(self._length):
            if self._array[i] == old_obj:
                self._array[i] = new_obj
        
    def remove(self, obj):
        for i in range(self._length):
            if self._array[i] == obj:
                index = self._array.index(obj)
                for j in range(index, self._length-1):
                    self._array[j] = self._array[j + 1]
                self._array[self._length - 1] = None
                self._length -= 1
    
    def insert(self, i, obj):
        if 0 < i < self._length:
            raise IndexError('invalid index')
        