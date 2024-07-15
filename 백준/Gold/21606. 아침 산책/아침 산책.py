import sys

input = sys.stdin.readline

class Vertex:
    def __init__(self, key: int, value: any=None) -> None:
        self.key = key
        self.value = value
        self.conn: list[int] = [] # connected to _

N = int(input())
vertexes: dict[int, Vertex] = {}
for i, v in enumerate(list(input().rstrip()), 1):
    vertexes[i] = Vertex(i, int(v))
for _ in range(N-1):
    a, b = map(int, input().split())
    vertexes[a].conn.append(b)
    vertexes[b].conn.append(a)

cache: dict[int, list] = {i: [] for i in range(1, N+1)}
visited = []
def dfs(start: int, v: Vertex) -> None:
    if v.key != start and v.value == 1:
        cache[start].append(v.key)
        cache[v.key].append(start)
    else:
        for next in v.conn:
            if next not in visited and next not in cache[start]:
                dfs(start, vertexes[next])

for i in range(1, N+1):
    if vertexes[i].value == 0:
        continue
    visited.append(i)
    dfs(i, vertexes[i])
    print(cache)

print(sum(map(len, cache.values())))