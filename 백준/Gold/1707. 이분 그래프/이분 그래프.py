import sys
from collections import deque

input = sys.stdin.readline

class Vertex:
    def __init__(self, key: int) -> None:
        self.key = key
        self.value = None
        self.conn = []

def main() -> None:
    def bfs(n: int) -> bool:
        visited = set()
        q = deque()
        
        for start in range(1, n + 1):
            if start not in visited:
                q.append(start)
                vertexes[start].value = 0
                while q:
                    v = q.popleft()
                    if v in visited:
                        continue
                    visited.add(v)
                    for i in vertexes[v].conn:
                        if vertexes[i].value is None:
                            vertexes[i].value = (vertexes[v].value + 1) % 2
                            q.append(i)
                        elif vertexes[i].value == vertexes[v].value:
                            return False
        return True

    N = int(input())
    for _ in range(N):
        V, E = map(int, input().split())
        A = [tuple(map(int, input().split())) for _ in range(E)]
        vertexes = {i: Vertex(i) for i in range(1, V + 1)}
        for a, b in A:
            vertexes[a].conn.append(b)
            vertexes[b].conn.append(a)

        print("YES" if bfs(V) else "NO")

if __name__ == "__main__":
    main()
