import sys
from collections import deque

input = sys.stdin.readline

def main() -> None:
    N, M, K, X = map(int, input().split())
    roads = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        frm, to = map(int, input().split())
        roads[frm].append(to) if to not in roads[frm] else None
    
    q = [i for i in roads[X]]
    visited = {X: 1}
    for _ in range(K-1):
        visit_now = q
        q = []
        for now in visit_now:
            visited[now] = 1
            q.extend([i for i in roads[now] if i not in visited and i not in visit_now and i not in q])
    
    print(*sorted(q) if q else [-1], sep="\n")

main()