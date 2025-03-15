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
                
      
       
primes_list = generate_primes(10)
print(primes_list)