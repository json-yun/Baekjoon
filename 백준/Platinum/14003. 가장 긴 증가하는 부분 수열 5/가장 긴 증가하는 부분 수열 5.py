import random

N = int(input())
seq = list(map(int, input().split()))
# seq = iter([random.randrange(-1000000000, 1000000000) for _ in range(N)])

A = [] # [list]

def bin_search(target, array):
    lo, hi = -1, len(array)
    
    while lo+1 < hi:
        mid = (lo+hi) // 2
        if array[mid] < target:
            lo = mid
        else:
            hi = mid

    return hi

dp = [] # len: LIS길이
dp_idx = [] # dp배열 원소의 위치 인덱스
prev = [i for i in range(N)] # len: 입력 배열의 길이

# dp.append(seq[0])
# dp_idx.append(0)
# prev[0] = 0
for i, num in enumerate(seq):
    j = bin_search(num, dp)
    # 갱신할 때
    if j < len(dp):
        dp[j] = num
        prev[i] = dp_idx[j-1] if j > 0 else i
        dp_idx[j] = i
    # 추가할 때
    else:
        dp.append(num)
        prev[i] = dp_idx[j-1] if j > 0 else i
        dp_idx.append(i)

# backtrace
cur = dp_idx[-1]
result = []
result.append(seq[cur])
while prev[cur] != cur:
    cur = prev[cur]
    result.append(seq[cur])

print(len(result))
print(*reversed(result))