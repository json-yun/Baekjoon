N, M = map(int, input().split())
A = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    A[a-1][b-1] = A[b-1][a-1] = 1

D = int(input())

def matrix_multiply(A: list[list[int]], B: list[list[int]]):
    C = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            C[i][j] = C[j][i] = sum(A[i][k] * B[j][k] for k in range(N)) % 1000000007

    return C

def matrix_power(arr: list[list[int]], n: int):
    if n in cache:
        return cache[n]
    
    a = n // 2
    b = n - a

    result = matrix_multiply(matrix_power(arr, a), matrix_power(arr, b))
    cache[n] = result
    return result

cache = {1: A}

print(matrix_power(A, D)[0][0])