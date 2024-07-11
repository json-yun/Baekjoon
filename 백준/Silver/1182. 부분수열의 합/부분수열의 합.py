import sys

N, S = [int(i) for i in sys.stdin.readline().split()]
A = [int(i) for i in sys.stdin.readline().split()]

def find_sum(level: int, total: int) -> int:
    count = 0
    if level < N-1:
        count += find_sum(level+1, total)
    total += A[level]
    if total == S:
        count += 1
    if level < N-1:
        count += find_sum(level+1, total)
    return count

print(find_sum(0, 0))