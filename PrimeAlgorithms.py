from warnings import warn

def generate_primes(limit):
    '''
    Returns a list of prime numbers upto and including limit
    '''
    
    if limit > 10**7:
        warn('This method is inefficient for generating prime numbers this large. Consider using another method.', category=RuntimeWarning)   
    
    primes = [True] * (limit + 1)
    primes[0] = False
    primes[1] = False
    
    for num in range(2, limit+1):
        if primes[num]:
            for multiple in range(num*num, limit+1, num):
                primes[multiple] = False
                
    return [i for i, j in enumerate(primes) if j]


def search(table: list[int], a: int):
    print(f'searching for {a} in partition {table}')
    mid = (len(table)-1) // 2
    
    if a == table[mid] or len(table) == 1:
        # found
        return table[mid]
    elif a > table[mid]:
        # search the right partition
        return search(table[mid+1:len(table)], a)
    elif a < table[mid]:
        # search the left partition
        return search(table[0:mid], a)
    # elif len(table) == 1:
    #     return table[0]

def find_next_prime(num):
    '''
    Return a prime number immediately larger than the given number
    '''
    primes = generate_primes(53)    
    return search(primes, num)
    
                
      
       
# primes_list = generate_primes(10)
# print(primes_list)
print(find_next_prime(21))