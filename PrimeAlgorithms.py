from warnings import warn
from math import ceil, floor

def generate_primes(limit):
    '''
    Returns a list of prime numbers upto and including limit
    O(n log(log(n))) why?
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

def find_next_prime(num):
    '''
    Return a prime number immediately larger than the given number
    '''
    primes = generate_primes(53)    
    return search(primes, num)
    
                
def is_prime(num):
    return search(generate_primes(num), num) == num


def log(base, num, percision=10e-6):
    if base <= 1:
        raise ValueError(f'base cannot be greater than 1. Instead was given {base}')
    if num <= 0:
        raise ValueError(f'Operand must be greater than 0. Instead was given {num}')

    low, high = 0, num
    
    while (high - low) > percision:
        mid = (low + high) / 2
        power = base**mid

        if abs(power - num) <= percision:
            return mid
        elif power > num:
            high = mid
        else:
            low = mid

    return (low + high) / 2


def find_next_power_2(num):
    return ceil(log(2, num))


# def power(base, exponent, precision=10e-6):


#     fraction = floor(exponent) - exponent
#     result = 1


#     for _ in range(floor(exponent)):
#         result *= base

#     if fraction < 0:
#         low, high = 1, base

#         while (high - low > precision):
#             mid = (low + high) / 2
#             if power(base, mid)



            
def unique(L: list[int]) -> int:
    result = 0
    for num in L:
        result = result ^ num
    return result


from random import shuffle

# L = [1, 3, 2, 1, 4, 4, 2]
# print(L)
# shuffle(L)
# print(L)

# print(unique(L))

size = 54
print(2 ** ceil(log(2, size * 2)))