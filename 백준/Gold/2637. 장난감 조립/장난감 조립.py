import sys
from collections import deque

input = sys.stdin.readline

class Vertex:
    def __init__(self, key: int) -> None:
        self.key = key
        self.inbound: list[tuple[int, int]] = [] # (키, 가중치)
        self.outbound: int = 0
        self.quantity: int = 0

def main() -> None:
    N = int(input())
    M = int(input())
    vertexes: dict[int, Vertex] = {}
    q = deque()
    # 데이터 불러오기
    for _ in range(M):
        to, frm, quantity = map(int, input().split())
        if frm not in vertexes:
            vertexes[frm] = Vertex(frm)
        if to not in vertexes:
            vertexes[to] = Vertex(to)
        vertexes[frm].outbound += 1
        vertexes[to].inbound.append((frm, quantity))
    
    # 최초 큐 삽입
    vertexes[N].quantity = 1
    q.append(N)
    while q:
        curr = q.popleft()
        for key, weight in vertexes[curr].inbound:
            vertexes[key].quantity += vertexes[curr].quantity * weight
            vertexes[key].outbound -= 1
            if vertexes[key].inbound and vertexes[key].outbound <= 0:
                q.append(key)
        del vertexes[curr]
        
    for v in sorted(vertexes):
        print(vertexes[v].key, vertexes[v].quantity)
    
if __name__ == "__main__":
    main()