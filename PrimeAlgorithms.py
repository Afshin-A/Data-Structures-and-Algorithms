from warnings import warn
from fractions import Fraction
from decimal import Decimal, getcontext

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


def next(table: list[int], a: int):
    '''
    Binary search for a number in a list. Returns the number or the next largest number 
    '''
    mid = (len(table)-1) // 2
    
    if a == len(table) == 1 or table[mid]:
        # found
        return table[mid]
    elif a > table[mid]:
        # search the right partition
        return next(table[mid+1:len(table)], a)
    elif a < table[mid]:
        # search the left partition
        return next(table[0:mid], a)


def find_next_prime(num):
    '''
    Return a prime number immediately larger than the given number
    '''
    primes = generate_primes(53)    
    return next(primes, num)
    
                
def is_prime(num):
    '''
    Returns if the given number is prime
    '''
    return next(generate_primes(num), num) == num
 
       
def gcd(a, b):
    '''
    Returns the greatest common divisor of the two numbers
    '''
    if b == 0:
        return a
    return gcd(b, a % b)


def num_decimal_places(num):
    '''
    Returns how many decimal places are in a number
    Example: 10.234 returns 3 while 10 returns 0
    '''
    count = 0
    # while there's decimals
    while num != int(num):       
        num *= 10
        count += 1
    return count
    
    
def power(base, exponent, precision=10e-6):
    if exponent == 0:
        return 1
    
    negative_exponent = exponent < 0
    decimal_places = num_decimal_places(exponent)
    decimal = round(exponent - int(exponent), decimal_places)
    exponent = abs(int(exponent))
    o_base = base
    
    binary = num_to_base(exponent, 2).reverse()
    results = 1

    for i in binary:
        if i:
            results *= base
        base **= 2
        
    # if exponent has decimal places
    if decimal != 0:
        denominator = power(10, decimal_places)
        numerator = round(denominator * decimal, decimal_places)
        
        # converting decimal into a fraction
        common_denominator = gcd(numerator, denominator)
        denominator /= common_denominator
        numerator /= common_denominator
        
        # initial guess
        guess = base / 2
        while abs(power(guess, denominator)-o_base) > precision:
            # newton's method for approximating the root
            guess = (((denominator - 1) * guess) + (o_base / (guess**(denominator-1)))) / denominator
        
        guess = power(guess, numerator)
        results *= guess
        
    if negative_exponent:
        return 1/results
        
    return results


def power_efficient(base, exponent, precision=10e-6):
    '''
    A more accurate and safe version of the power function
    This function uses the decimal class to perform accurate calculations without the risk of integer overflow 
    This is possible because the Decimal object stores base and exponent of a number separately
    In addition, the function uses the Fraction class for simpler 
    '''
    if exponent == 0:
        return 1
    
    # setting the number of significant figures in calculations performed by Decimal
    getcontext().prec = 50
    base = Decimal(base)
    base_copy = base
    result = Decimal(1)
    exponent = Decimal(exponent)
    
    is_negative_exponent = exponent < 0
    exponent = abs(exponent)
    
    exponent_int = int(exponent)
    exponent_decimal = exponent - exponent_int
    
    binary = num_to_base(exponent_int, 2)
    binary.reverse()
    for bit in binary:
        if bit:
            result *= base
        base *= base
        
    if exponent_decimal != 0:
        fraction = Fraction(exponent_decimal).limit_denominator(1000)
        numerator, denominator = fraction.numerator, fraction.denominator
        
        base = base_copy
        guess = base / 2
        while abs(power_efficient(guess, denominator)-base) > precision:
            guess = (((denominator - 1) * guess) + (base / (guess**(denominator-1)))) / denominator
        
        guess = power_efficient(guess, numerator)
        result *= guess
        
    if is_negative_exponent:
        return 1/result
        
    return result
        

def num_to_base(num: int, base: int) -> list[int]:
    '''
    Converts a given number in the specified base
    Example: num_to_base(100, 2) returns the binary representation of 100
    '''
    if num < 0:
        raise ValueError('This algorithm does not support negative numbers')
    if base < 2:
        raise ValueError('This algorithm supports a minimum base of 2')
    
    if num == 0:
        return [0]
    
    quotient = num
    results = []
    
    # list of possible digits upto to 'F' representing 0-15
    digits = {
        i: i for i in range(16)    
    }
    for i in range(10, 16):
        digits[i] = chr(55 + i)
    
    # more succinct way of generating the numbers
    # remainders = { i: hex(i)[2:].upper() for i in range(16)}

    while quotient:
        results.append(digits[quotient % base])
        quotient //= base
    
    results.reverse()
    return results


def exponentiate(base, exponent):
    '''
    Rudimentary power function that calculates base^exponent using the method of exponentiation by squares
    Does not support fraction exponents
    '''
    if exponent == 0:
        return 1
    
    decimal_places = num_decimal_places(exponent)
    fraction = round(exponent - int(exponent), decimal_places)
    exponent = int(exponent)
    
    binary = num_to_base(exponent, 2)
    
    results = 1
    # for i in reversed(binary):
    for i in binary:
        if i:
            results *= base
        base **= 2
        
    return results
    

def log(base, num, precision=10e-6):
    # 0 < log_{base} < num/2
    # we can verify this graphically 
    
    start = 0
    end = num/2
    
    while abs(start-end) > precision:
        guess = (start+end)/2
        power_guess = power_efficient(base, guess)
        if abs(power_guess-num) < precision:
            return guess
        elif power_guess < num:
            start = guess
        else:
            end = guess
            
    return (start + guess) / 2


def next_power_of_2(num):
    '''using bitwise operations, returns the next power of 2 greater or equal than 
    the given number'''
    binary_digits = 0
    while num > 0:
        num = num >> 1
        binary_digits += 1    
    return 1 << binary_digits

# print(log(20, 11))

# print(power_efficient(2, 2.1))
# print(next_power_of_2(16))