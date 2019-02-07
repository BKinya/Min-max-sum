#check if prime
def isPrime(n):
    if n < 2: return "Neither prime, nor composite"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#return the nth prime number
def findNthPrimeNumber(n):
    position = 0
    primeNumber = 1

    while position < n:
         primeNumber += 1
         if isPrime(primeNumber):
             position += 1
    return primeNumber

print(findNthPrimeNumber(10001))
    


