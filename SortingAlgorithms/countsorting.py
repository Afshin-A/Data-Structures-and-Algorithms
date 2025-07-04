
l = [2, 2, 8, 5, 2, 3, 5]



def find_min_max(arr):
    '''
    More efficient way of finding min and max in a list
    We compare elements in a pair which results in 3 comparisons per 2 elements
    Normally there would be 2 comparisons per 1 element
    '''
    if len(arr) % 2 == 0:
        if arr[0] < arr[1]:
            smallest, largest = arr[0], arr[1]
        else:
            smallest, largest = arr[1], arr[0]
        i = 2
    else:
        smallest, largest = arr[0], arr[0]
        i = 1
        
    while i < len(arr) - 1:
        a, b = arr[i], arr[i+1]
        if a < b:
            # a is the minimum of a and b
            # compare it with the overall minumum
            if a < smallest:
                smallest = a
            if b > largest:
                largest = b
        else:
            # b is the minumum
            if b < smallest:
                smallest = b
            if a > largest:
                largest = a
        i += 2
        
    return smallest, largest
            


def CountingSort(l: list[int]):
    '''
    This is the unstable implementation. Use the CountingSortStable version for the stable implementation
    
    Time complexity: O(len(l)+max(l))
    
    Performs the counting sort algorithm
    
    Modifies the original array in place
    
    Assumes l is a list of integers. Negatives integers are allowed
    
    Other notes:
    - This algorithm is not feasable for small arrays with large values, because we need a counter-array of length max(array)
    - The general rule of thumb is that counting sort algorithm is competitive if  max(l) <= 10*len(l) if an array of len 10 can have a max element of 100 and it would still be okay
    - The smaller the max value, the better
    - Only works on integers
    - It can work on negative numbers, but makes the algorithm slightly more complex
        - Strategy 1: We can find the min value, subtract it from all elements in the array, sort the array, then add it back to all elements in the array
        - Strategy 2: define an offset variable. If the smallest value is -2, then we shift everything by 2 in the counter array. 

    '''
    
    # First find the smallest and largest element in the array
    min_val = max_val = l[0]

    for num in l:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    
    r = max_val - min_val + 1
    offset = 0 - min_val
    
    # Create a counter array that maps element (index) to the number of times that element was seen in the original array    
    counter = [0] * r
    # O(l)
    for elem in l:
        counter[elem+offset] += 1

    i = 0
    # O(max(l))
    for j in range(len(counter)):
        # ignore 0s
        # while the count is not 0
        while counter[j]:
            # 
            l[i] = j - offset
            i += 1
            counter[j] -= 1

# print(l)
# CountingSort(l)
# print(l)        



def CountingSortStable(arr: list):
    # find min and max values
    min_val, max_val = find_min_max(arr)
    # find range of values
    r = max_val - min_val + 1
    # if the smallest value is 2, for example, our counter array would look like [0, 0, 1 ...]
    # to avoid the leading 0s before 4, we use an offset to shift the entire array to the left. In essense, we map the smallest value to the index 0 
    # in order to save some space
    offset = 0 - min_val
    
    counter = [0] * r
    for elem in arr:
        counter[elem + offset] += 1
    
     
    # we can use the prefix sum of the counter to find positions of elements in the final, sorted array
    
    # Since we're only using the commutative sum one time, we can use a simple loop
    # if there were lots of updates, I would use a fenwick tree
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]
    
    # this stores our results
    results = [0] * r
    
    # we traverse the array backwards
    # if the last element is 5, we find it's position in the counter
    # if the commutative sum for 5 is 6, that means there are 6 elements that <= 5
    # 5 would be the of those elements
    # so the index of 5 would be 5
    # then we need to decrement the counter value
    # if there is another 5, it will have the index of 4
    # this way we preserve the order for repeat values
    for elem in arr[::-1]:
        counter[elem + offset] -= 1
        results[counter[elem + offset]] = elem
    
    print(results)
    return results

CountingSortStable(l)