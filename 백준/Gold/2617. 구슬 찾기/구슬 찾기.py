import sys
from collections import deque

input = sys.stdin.readline

class Vertex:
    def __init__(self, key: int) -> None:
        self.key = key
        self.outbound: list[int] = []
        self.inbound: list[int] = []
        self.nth_left: int = 0
        self.nth_right: int = 0

def main() -> None:
    N, M = map(int, input().split())
    vertexes: dict[int, Vertex] = {i: Vertex(i) for i in range(1, N+1)}
    for _ in range(M):
        frm, to = map(int, input().split())
        if frm == to:
            continue
        vertexes[frm].outbound.append(to)
        vertexes[to].inbound.append(frm)
    
    def dfs_right(i):
        visited[i] = 1
        # if vertexes[i].nth_right:
        #     return vertexes[i].nth_right
        level = 1
        for v in vertexes[i].outbound:
            if v not in visited:
                level += dfs_right(v)
        # vertexes[i].nth_right = level
        return level
    
    def dfs_left(i):
        visited[i] = 1
        # if vertexes[i].nth_left:
        #     return vertexes[i].nth_left
        level = 1
        for v in vertexes[i].inbound:
            if v not in visited:
                level += dfs_left(v)
        # vertexes[i].nth_left = level
        return level
    
    for i in range(1, N+1):
        visited = {}
        vertexes[i].nth_left = dfs_left(i)
        visited = {}
        vertexes[i].nth_right = dfs_right(i)
    
    mid = N // 2 +1
    result = sum((vertexes[i].nth_left > mid or vertexes[i].nth_right > mid) for i in vertexes)
    print(result)
    
if __name__ == "__main__":
    main()