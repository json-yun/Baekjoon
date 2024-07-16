import sys
from collections import deque

input = sys.stdin.readline

di = (1, 0, 0, -1, 0, 0)
dj = (0, 1, -1, 0, 0, 0)
dk = (0, 0, 0, 0, 1, -1)

def main() -> None:
    def age(q: deque) -> None:
        next_q = deque()
        while q:
            k, i, j = q.popleft()
            for d in range(6):
                new_i, new_j, new_k = i+di[d], j+dj[d], k+dk[d]
                if all((0<=new_i<N, 0<=new_j<M, 0<=new_k<H)):
                    if A[new_k][new_i][new_j]==0:
                        A[new_k][new_i][new_j] = 1
                        next_q.append((new_k, new_i, new_j))
        return next_q
    
    def check_zero():
        for k in A:
            for i in k:
                for j in i:
                    if j == 0:
                        return True
        return False

    M, N, H = map(int, input().split())
    A = []
    q = deque()
    n_0 = 0
    for k in range(H):
        A.append([])
        for i in range(N):
            A[k].append([])
            for j, e in enumerate(input().split()):
                e = int(e)
                A[k][i].append(e)
                if e == 1:
                    q.append((k, i, j))
                elif e == 0:
                    n_0 += 1
    count = 0
    while q:
        q = age(q)
        if q:
            count += 1
    if check_zero():
        print(-1)
    else:
        print(count)
    
main()