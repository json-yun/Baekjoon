import sys
from collections import deque

input = sys.stdin.readline

class Vertex:
    def __init__(self, key: int) -> None:
        self.key: int = key
        self.adj_vector: list = []

def main() -> None:
    def find_no_outbound(include: list) -> list:
        for i in include:
            flag = True
            for j in include:
                if vertexes[i].adj_vector[j-1]:
                    flag = False
                    break
            if flag:
                include.remove(i)
                return i
        return None
    N = int(input())
    vertexes: dict[int, Vertex] = {i: Vertex(i) for i in range(1, N+1)}
    # 데이터 불러오기
    for i in range(1, N+1):
        vertexes[i].adj_vector = list(map(int, list(input().rstrip())))
    
    waiting = list(reversed(vertexes.keys()))
    n = N
    while waiting:
        next = find_no_outbound(waiting)
        if next is None:
            print(-1)
            return
        vertexes[next].key = n
        n -= 1
    # flag = True
    # for i in range(1, N+1):
    #     if vertexes[i].key != i:
    #         flag = False
    #         break
    # if flag:
    #     print(-1)
    #     return
    print(*[vertexes[i].key for i in range(1, N+1)])
    
if __name__ == "__main__":
    main()