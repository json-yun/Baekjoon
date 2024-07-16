import sys
from collections import deque

input = sys.stdin.readline
di = (1, 0, 0, -1)
dj = (0, 1, -1, 0)

def main() -> None:
    # MAP를 1칸씩 확장하는 함수
    def expand(map):
        for i in range(N):
            for j in range(N):
                for d in range(4):
                    new_i, new_j = i+di[d], j+dj[d]
                    if not all((0<=new_i<N, 0<=new_j<N)):
                        continue
                    MAP[i][j] += map[new_i][new_j]
            
    # map_cur를 전체 방으로 맞춰주는 함수
    def check_room(map: list, edge: deque) -> deque:
        # visited = map
        q = edge.copy()
        edge = deque()
        q.append((0, 0))
        # (q.append(i) for i in edge)
        while q:
            cur = q.popleft()
            flag = False
            for d in range(4):
                new_i, new_j = cur[0]+di[d], cur[1]+dj[d]
                if not all((0<=new_i<N, 0<=new_j<N)):
                    continue
                if MAP[new_i][new_j] != 0:
                    if map[new_i][new_j] == 0:
                        map[new_i][new_j] = 1
                        q.append((new_i, new_j))
                else:
                    flag = True
            if flag:
                edge.append(cur)
        return edge
        
    N = int(input())
    MAP = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    map_cur = [[0]*N for _ in range(N)]
    map_cur[0][0] = 1
    edge = deque()
    
    n_change = 0
    edge = check_room(map_cur, edge)
    # print(*map_cur, sep="\n")
    while map_cur[N-1][N-1]==0:
        n_change += 1
        expand(map_cur)
        edge = check_room(map_cur, edge)
        # print()
        # print(*map_cur, sep="\n")
    print(n_change)
main()