import sys
from collections import deque

input = sys.stdin.readline

def main() -> None:
    def bfs() -> int:
        q = deque()
        q.append((0, 0))
        while q:
            now = q.popleft()
            for i in range(4):
                new_i = now[0]+dx[i]
                new_j = now[1]+dy[i]
                if (new_i, new_j) == (N-1, M-1):
                    return A[now[0]][now[1]]+1
                if 0 <= new_i < N and 0 <= new_j < M and A[new_i][new_j] == 1:
                    A[new_i][new_j] += A[now[0]][now[1]]
                    q.append((new_i, new_j))
            A[now[0]][now[1]] = 0

    N, M = map(int, input().split())
    A = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    dx = (1, 0, 0, -1)
    dy = (0, 1, -1, 0)
    print(bfs())

main()