import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
graph: list[tuple] = []

for _ in range(E):
    a, b, weight = map(int, input().split())
    graph.append((a, b, weight))

graph.sort(key=lambda x: x[2])

tree = {i: i for i in range(1, V+1)} # dict[vertex, parent]
def find_root(v):
    if tree[v] != v:
        tree[v] = find_root(tree[v]) # 경로압축

    return tree[v]
        
total = 0
cnt = 0
for a, b, weight in graph:
    if cnt >= V-1:
        break
    if (p_a:=find_root(a)) != (p_b:=find_root(b)):
        # 부분트리의 루트를 비교한다.
        tree[max(p_a, p_b)] = min(p_a, p_b)
        total += weight
        cnt += 1

print(total)