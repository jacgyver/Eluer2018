
def isPrime(num):
    if num == 2 or num == 3:
        return True

    if (num % 2 == 0 or num % 3 == 0):
        return False

    for i in range(4,int(num/2)):
        if (num % i == 0):
            return False
    return True

def prime_factor(num):
    factor_list = []
    for i in range(2,int(num/2)):
        if (isPrime(i)):
            if (num % i == 0):
                factor_list.append(i)
                print(factor_list)

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

get_primes(13195)
#prime_factor(600851475143)


