import sys

def make_edge(x: str | int, 
              y: str | int, 
              weight: str | int) -> tuple[int, tuple[int]]:
    return (int(weight), (min(int(x), int(y)), max(int(x), int(y))))

def main() -> None:
    def find_parent(i: int) -> int:
        while parents[i] != i:
            i = parents[i]
        return i
    
    V, E = [int(i) for i in sys.stdin.readline().split()]
    EDGES = sorted([make_edge(*sys.stdin.readline().split()) for _ in range(E)], key=lambda x: x[0], reverse=True)

    parents = {i: i for i in range(1, V+1)}
    min_weight = 0
    count = 1
    while count < V:
        weight, e = EDGES.pop()
        if (p0:=find_parent(e[0])) != (p1:=find_parent(e[1])):
            count += 1
            min_weight += weight
            parents[p1] = p0
            parents[e[0]] = p0
        elif e[0] == e[1] and weight < 0:
            min_weight += weight

    print(min_weight)

main()