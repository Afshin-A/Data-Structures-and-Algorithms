
class SegmentTree:
    def __init__(self, A_1):
        '''
        time complexity: O(log(n))
        '''
        # size of original array
        self.n = len(A_1)    
        
        n_2 = 2*self.n
        # new array is twice as large as the old array
        A_2 = [None] * (self.n * 2)

        # add original array content to the end of new array
        for k in range(self.n):
            A_2[self.n + k] = A_1[k]
        
        # starting at the last two indices of new array
        j = (2*self.n)-1
        i = j-1
        
        # when done, array format is [None, #, #, # ...] so we stop when the smaller index is 1 or 0
        while i > 1:
            # find parrent
            p = j//2
            A_2[p] = max(A_2[i],  A_2[j])
            # we compare two indices at a time
            j -= 2
            i -= 2
            
        # rename array for better clarity
        self._A = A_2
        
        
    def update(self, i, val):
        '''
        worst time complexity: O(log(n))
        '''
        # shift i to second half of A
        i += self.n
        
        if i >= len(self._A):
            raise ValueError('index too large')
        
        while i > 1:
            # update index
            self._A[i] = val
            
            # find parrent
            p = i // 2
            
            # do we compare i with left index or right?
            # It depends if it's even or odd
            # in binary, all even numbers end with 0. so if i & 1 returns 0, i is even. otherwise, it's odd
            if (i & 1 == 0):
                # if even, we compare it with the right neighbor
                j = i + 1
            else:
                # if odd, we compare it with the left neighbor
                j = i - 1
            
            # calculate parent value
            new_parent_val = max(self._A[i], self._A[j])
            
            # if the update didn't affect the parent value (i.e. the parent already equals the new value),
            # then all grandparents remain the same and we're done.
            if self._A[p] == new_parent_val:
                return
            else:
                self._A[p] = new_parent_val
            
            # update i    
            i = p
            
            # NOTE: we can simplify the code and skip checking for the parity (odd or even) of i
            # i //= 2
            # new_parent_val = max(self._A[2*i], self._A[2*i+1])
                
                
    def rangeQuery(self, i, j):
        '''
        Returns the maximum value in [i, j]
        Worst time complexity: O(log(n))
        '''
        # user enters i and j with respect to original array. we adapt the indices so they point to their new positions in the new array with double capacity
        i += self.n
        j += self.n
        
        # initially set maximum to smallest possible value
        maximum = float('-inf')
        
        # while elements exist in the range (note that when i==j, there's still 1 element to be processed because i and j are inclusive)
        while (i <= j):
            print(f'[{self._A[i]}, {self._A[j]}]')
            # if i is odd, it is a right child with respect to its parent
            # the parent cannot represent the range because the parent also represents the left child and the left child is not in the query range
            if (i & 1) == 1:
                # we include the right child in the search
                maximum = max(maximum, self._A[i])
                # we increment i to an even index, which is a left child.
                i += 1
            
            # NOTE: if i is even, then we do nothing because its parent already represents the range query. 
            
            if (j & 1) == 0:
                maximum = max(maximum, self._A[j])
                j -= 1
            
            # go to parent indices
            # bitwise right shift is equivalent to integer dividing by 2
            i >>= 1
            j >>= 1
            print(maximum)
                        
        return maximum

    def __str__(self):
        return str(self._A)

st = SegmentTree([7, 1, 0, 9, 2])
# st.update(2, 10)
print(st)
st.rangeQuery(0, 3)
