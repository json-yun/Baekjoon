import sys

N, S = [int(i) for i in sys.stdin.readline().split()]
A = [int(i) for i in sys.stdin.readline().split()]

def find_sum(index: int, total: int) -> int:
    count = 0
    # 현재 index의 값을 더하지 않고 진행한 경우
    if index < N-1:
        count += find_sum(index+1, total)
    # 현재 index의 값을 더하고 진행한 경우
    total += A[index]
    if total == S:
        count += 1
    if index < N-1:
        count += find_sum(index+1, total)
    return count

print(find_sum(0, 0))