import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

gems = [tuple(map(int, input().split())) for _ in range(N)]
knapsacks = [int(input()) for _ in range(K)]

gems.sort()
knapsacks.sort()

total_value = 0
base = 0
pool = []
for capacity in knapsacks:
    for i in range(base, N):
        if capacity < gems[i][0]:
            break
        heapq.heappush(pool, -gems[i][1])
    else:
        i = N
    base = i

    if pool:
        total_value += -heapq.heappop(pool)

print(total_value)
