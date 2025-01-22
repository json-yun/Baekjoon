import heapq
import sys

input = sys.stdin.readline

class heap(list):
    def __init__(self):
        return super().__init__()

    def push(self, elem):
        heapq.heappush(self, elem)

    def pop(self):
        return heapq.heappop(self)

N = int(input())
poes = [tuple(sorted(map(int, input().split()))) for _ in range(N)]
D = int(input())

poes.sort(key=lambda x: x[1])

max_l = 0
q = heap()
for po in poes:
    q.push(po)
    rb = po[1]
    lb = rb - D

    while len(q) > 0 and q[0][0] < lb:
        q.pop()
    else:
        if (lq:=len(q)) > max_l:
            max_l = lq

print(max_l)