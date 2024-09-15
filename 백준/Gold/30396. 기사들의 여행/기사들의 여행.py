import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline
BOARD_SIZE = 4
di = (-2, -2, -1, -1, 1, 1, 2, 2)
dj = (-1, 1, -2, 2, -2, 2, -1, 1)

MOVEMAP = []
for a in range((BOARD_SIZE+1)//2):
    temp = []
    for b in range((BOARD_SIZE+1)//2):
        q = deque()
        board = [[10,10,10,10],
                [10,10,10,10],
                [10,10,10,10],
                [10,10,10,10]]
        q.append((a, b, 0))

        cnt = BOARD_SIZE**2
        while cnt:
            i, j, c = q.popleft()
            if c < board[i][j]:
                board[i][j] = c
                cnt -= 1
            for d in range(8):
                if 0<=i+di[d]<4 and 0<=j+dj[d]<4:
                    q.append((i+di[d], j+dj[d], c+1))
        temp.append(board)
    MOVEMAP.append(temp)

def main() -> None:
    # board에서 나이트 좌표를 deque로 반환
    def find_knight(board: list[list[int]], 
                    constraints: callable = (lambda x: True)) -> list:
        knights = []
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if constraints((i, j)):
                    for _ in range(cell):
                        knights.append((i, j))

        return knights

    def rotated(pos: tuple[int], degree: int) -> tuple[int]:
        match degree:
            case 0:
                return pos
            case 90:
                return (pos[1], BOARD_SIZE-1-pos[0])
            case 180:
                return (BOARD_SIZE-1-pos[0], BOARD_SIZE-1-pos[1])
            case 270:
                return (BOARD_SIZE-1-pos[1], pos[0])

        raise
        
    INIT = [list(map(int, list(input().rstrip()))) for _ in range(BOARD_SIZE)]
    TARGET = [list(map(int, list(input().rstrip()))) for _ in range(BOARD_SIZE)]
    
    knights = find_knight(INIT, lambda x: not TARGET[x[0]][x[1]])
    target_pos = find_knight(TARGET, lambda x: not INIT[x[0]][x[1]])

    moves = []
    for knight in knights:
        moves_x = []
        if BOARD_SIZE//2 <= knight[0]:
            if BOARD_SIZE//2 <= knight[1]:
                degree = 180
            else:
                degree = 90
        else:
            if BOARD_SIZE//2 <= knight[1]:
                degree = 270
            else:
                degree = 0
        rotated_knight = rotated(knight, degree)
        for target in target_pos:
            rotated_target = rotated(target, degree)
            n_moves = MOVEMAP[rotated_knight[0]][rotated_knight[1]][rotated_target[0]][rotated_target[1]]
            moves_x.append(n_moves)
        moves.append(moves_x)

    min_ = float("inf")
    for cases in permutations(range(len(moves)), len(moves)):
        temp = 0
        for i, j in enumerate(cases):
            temp += moves[i][j]
        min_ = min(min_, temp)
        
    print(min_)

if __name__ == "__main__":
    sys.exit(main())