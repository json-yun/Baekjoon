import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

class Vertex:
    def __init__(self, key: int, value: any=None) -> None:
        self.key = key
        self.value = value
        self.conn: list[int] = [] # connected to _

N = int(input())
vertexes: dict[int, Vertex] = {}
outside = []
result = 0
visited = [0]*(N+1)
for i, v in enumerate(list(input().rstrip()), 1):
    vertexes[i] = Vertex(i, int(v))
    if v == '0':
        outside.append(i)
for _ in range(N-1):
    a, b = map(int, input().split())
    vertexes[a].conn.append(b)
    vertexes[b].conn.append(a)
    if vertexes[a].value + vertexes[b].value == 2:
        result += 2

def dfs(now: int) -> None:
    visited[now] = 1
    n_inside = 0
    for adj in vertexes[now].conn:
        if vertexes[adj].value == 1:
            n_inside += 1
            visited[adj] = 1
        elif not visited[adj]:
            n_inside += dfs(adj)
    return n_inside
        
for i in outside:
    if not visited[i]:
        n = dfs(i)
        result += n * (n-1)

print(result)