import sys
from collections import deque

input = sys.stdin.readline

class Vertex:
    def __init__(self, key: int) -> None:
        self.key = key
        self.value = None
        self.conn = [] # connected to _


def main() -> None:
    def bfs(n: int) -> bool:
        all_vertexes = set([i for i in range(1, n+1)])
        visited = set()
        q = deque()
        while len(visited) < n:
            start = (all_vertexes - visited).pop()
            q.append(start)
            vertexes[start].value = 0
            while len(q):
                v = q.popleft()
                visited.add(v)
                for i in vertexes[v].conn:
                    if i not in visited:
                        q.append(i)
                        if vertexes[i].value is None:
                            vertexes[i].value = (vertexes[v].value + 1) % 2
                        elif vertexes[i].value == vertexes[v].value:
                            return False
        return True
    
    N = int(input())
    for _ in range(N):
        V, E  = map(int, input().split())
        A = [list(map(int, input().split())) for _ in range(E)]
        vertexes = {i: Vertex(i) for i in range(1, V+1)}
        for a, b in A:
            vertexes[a].conn.append(b)
            vertexes[b].conn.append(a)
        
        print("YES" if bfs(V) else "NO")
        
main()