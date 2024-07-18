import sys
from collections import deque

input = sys.stdin.readline

def main() -> None:
    def infect(q: deque) -> deque:
        di = (1, 0, 0, -1)
        dj = (0, 1, -1, 0)
        next_q = deque()
        while q:
            i, j = q.popleft()
            for d in range(4):
                curr_i, curr_j = i+di[d], j+dj[d]
                if 0<=curr_i<N and 0<=curr_j<N and A[curr_i][curr_j] == 0:
                    A[curr_i][curr_j] = A[i][j]
                    next_q.append((curr_i, curr_j))
        
        return next_q
    
    N, K = map(int, input().split())
    q_virus = {i: deque() for i in range(1, K+1)}
    A = []
    for i in range(N):
        A.append([])
        for j, v in enumerate(map(int, input().split())):
            A[i].append(v)
            if v != 0:
                q_virus[v].append((i, j))
    S, X, Y = map(int, input().split())
    
    for _ in range(S):
        len_q = 0
        for n in range(1, K+1):
            q_virus[n] = infect(q_virus[n])
            len_q += len(q_virus[n])
        if len_q == 0:
            break
    
    print(A[X-1][Y-1])
    
if __name__ == "__main__":
    main()