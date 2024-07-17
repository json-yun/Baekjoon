import sys
from collections import deque

input = sys.stdin.readline

class Vertex:
    def __init__(self, key: int) -> None:
        self.key = key
        self.outbound: list[tuple[int, int]] = [] # (키, 가중치)
        self.inbound: int = 0
        self.max_sum_weight: int = 0
        self.route: set[tuple[int, int]] = set() # (출발, 도착)

def main() -> None:
    # 데이터 불러오기
    N = int(input())
    M = int(input())
    vertexes: dict[int, Vertex] = {}
    for _ in range(M):
        frm, to, weight = map(int, input().split())
        if frm not in vertexes:
            vertexes[frm] = Vertex(frm)
        if to not in vertexes:
            vertexes[to] = Vertex(to)
        vertexes[frm].outbound.append((to, weight))
        vertexes[to].inbound += 1
    START, END = map(int, input().split())
    
    # 최초 큐 삽입
    q: deque[int] = deque()
    q.append(START)
    while q:
        curr = q.popleft()
        for key, weight in vertexes[curr].outbound:
            if vertexes[key].max_sum_weight == (new_weight:=vertexes[curr].max_sum_weight + weight):
                vertexes[key].route.update(vertexes[curr].route | set([(curr, key)]))
            elif vertexes[key].max_sum_weight < new_weight:
                vertexes[key].max_sum_weight = new_weight
                vertexes[key].route = vertexes[curr].route | set([(curr, key)])
            vertexes[key].inbound -= 1
            if vertexes[key].inbound == 0:
                q.append(key)
        if curr != END:
           del vertexes[curr]
    print(vertexes[END].max_sum_weight, len(vertexes[END].route), sep="\n")
    
if __name__ == "__main__":
    main()