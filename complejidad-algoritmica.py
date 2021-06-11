import time


def factorial(n):
    respesta = 1

    while n > 1:
        respesta *= n
        n -= 1
    
    return respesta

def factorial_r(n):
    if n==1:
        return 1
    
    return n* factorial(n-1)


if __name__ == '__main__':
    n = 10000
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)
