class Hashtable:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._array = [None * capacity]
       
    def hash(self, num: int):
        return num % self.capacity
     
    def add(self, num: int):
        index = hash(num)
        self._array[index] = num
    
    def remove(self):
        pass
    
    def contains(self, num: int):
        index = self.hash(num)
        
        if self._array[index] == num:
            return True
        elif self._array[index] == -1 or self._array[index] == None:
            return False
        else:
            index += 1
    
    
    