import sys

input = sys.stdin.readline

class Vertex:
    def __init__(self, key: int) -> None:
        self.key: int = key
        self.adj_vector: list = []

def main() -> None:
    def find_no_outbound(include: list) -> list:
        for i in include:
            if all(not vertexes[i].adj_vector[j-1] for j in include):
                include.remove(i)
                return i
        return None
    # 데이터 불러오기
    N = int(input())
    vertexes: dict[int, Vertex] = {i: Vertex(i) for i in range(N, 0, -1)}
    for i in range(1, N+1):
        vertexes[i].adj_vector = list(map(int, list(input().rstrip())))
    
    waiting = list(vertexes.keys())
    n = N
    while waiting:
        next = find_no_outbound(waiting)
        if next is None:
            print(-1)
            return
        vertexes[next].key = n
        n -= 1
    print(*[vertexes[i].key for i in range(1, N+1)])
    
if __name__ == "__main__":
    main()