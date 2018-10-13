isPrime = [True] * 1000001

def isPrime2(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    return True

def isItPrime(N):
    for i in range(0, len(N)):
        if not isPrime2(i): N[i] = False

isItPrime(isPrime)
