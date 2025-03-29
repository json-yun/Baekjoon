import sys
from collections import deque

input = sys.stdin.readline
di = (1, 0, 0, -1)
dj = (0, 1, -1, 0)

def main() -> None:
    N, M = map(int, input().split())
    board: list[list[int]] = [list(map(int, tuple(input().strip()))) for _ in range(N)]


    def is_on_board(pos: tuple[int, int]) -> bool:
        i, j = pos
        if 0 <= i < len(board) and 0 <= j < len(board[0]):
            return True
        return False
    AVAILABLE = 0
    WALL = 1
    visited: list[list[int]] = [[False]*M for _ in range(N)]
    visited_break: list[list[int]] = [[False]*M for _ in range(N)]
    
    
    q = deque()
    q.append((0, 0, 1, True)) # (x, y, depth, canbreak)
    while q:
        i, j, depth, canbreak = q.popleft()
        if (i, j) == (N-1, M-1):
            result = depth
            break
        
        if visited[i][j]:
            continue
        if visited_break[i][j]:
            if canbreak:
                visited[i][j] = True
            else:
                continue
        if board[i][j] == AVAILABLE:
            if canbreak:
                visited[i][j] = True
            else:
                visited_break[i][j] = True
        
        for d in range(4):
            i_next, j_next = i+di[d], j+dj[d]
            if not is_on_board((i_next, j_next)):
                continue
            if visited[i_next][j_next]:
                continue
            if board[i_next][j_next] == WALL:
                if canbreak and not visited_break[i_next][j_next]:
                    q.append((i_next, j_next, depth+1, False))
                if not canbreak:
                    continue
            elif board[i_next][j_next] == AVAILABLE:
                q.append((i_next, j_next, depth+1, canbreak))

    else:
        result = -1
        
    print(result)

main()