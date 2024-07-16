import sys
from collections import deque

input = sys.stdin.readline

def main() -> None:
    N, M = map(int, input().split())
    inbound = {i: 0 for i in range(1, N+1)}
    outbound = {i: [] for i in range(1, N+1)}
    q = deque()
    for _ in range(M):
        frm, to = map(int, input().split())
        # if to not in outbound[frm]:
        outbound[frm].append(to)
        inbound[to] += 1
    
    for i in inbound.items():
        q.append(i[0]) if i[1] == 0 else None
    result = []
    while q:
        i = q.popleft()
        result.append(i)
        for j in outbound[i]:
            inbound[j] -= 1
            if inbound[j] == 0:
                q.append(j)
    print(*result)
    
if __name__ == "__main__":
    main()
    