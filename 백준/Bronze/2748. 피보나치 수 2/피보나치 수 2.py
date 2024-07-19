n = int(input())

cache = {0: 0,
        1: 1,
        2: 1}

def fibo(n: int) -> int:
    if n not in cache:
        cache[n] = fibo(n-2)+fibo(n-1)
    return cache[n]

print(fibo(n))