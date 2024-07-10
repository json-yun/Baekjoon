import sys
import heapq

N = int(sys.stdin.readline())
A = [int(sys.stdin.readline()) for _ in range(N)]

big = []
small = []
mid = A.pop(0)
bias = 0
for a in A:
    print(mid)
    if a < mid:
        if bias > 0:
            heapq.heappush(small, -a)
            bias -= 1
        else:
            heapq.heappush(big, mid)
            bias += 1
            heapq.heappush(small, -a)
            mid = -heapq.heappop(small)
    else:
        if bias < 0:
            heapq.heappush(big, a)
            bias += 1
        elif bias == 0:
            heapq.heappush(big, a)
            bias += 1
        else:
            heapq.heappush(small, -mid)
            bias -= 1
            heapq.heappush(big, a)
            mid = heapq.heappop(big)
print(mid)