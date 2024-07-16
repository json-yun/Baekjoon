import sys
from collections import deque

def main() -> None:
    def water_expand(waters: list) -> list:
        next_waters = []
        while waters:
            curr_w = waters.pop()
            for d in range(4):
                new_i, new_j = curr_w[0]+dx[d], curr_w[1]+dy[d]
                if all((0<=new_i<R, 0<=new_j<C)):
                    if A[new_i][new_j] not in ['D', 'X', '*']:
                        A[new_i][new_j] = '*'
                        next_waters.append((new_i, new_j))
        return next_waters
    def move_hedgehogs(hedgehogs: list) -> list | None:
        next_hedgehogs = []
        while hedgehogs:
            curr_h = hedgehogs.pop()
            if A[curr_h[0]][curr_h[1]] == '*':
                continue
            for d in range(4):
                new_i, new_j = curr_h[0]+dx[d], curr_h[1]+dy[d]
                if all((0<=new_i<R, 0<=new_j<C)):
                    if A[new_i][new_j] not in ['*', 'X', 'S']:
                        if A[new_i][new_j] in ['D']:
                            return None
                        A[new_i][new_j] = 'S'
                        next_hedgehogs.append((new_i, new_j))
        return next_hedgehogs
    
    input = sys.stdin.readline
    dx = (1, 0, 0, -1)
    dy = (0, 1, -1, 0)
    hedgehogs = []
    waters = []
    count = 0
    
    R, C = map(int, input().split())
    A = []
    for i in range(R):
        A.append([])
        for j, a in enumerate(list(input().rstrip())):
            A[i].append(a)
            if a == '*':
                waters.append((i, j))
            elif a == 'S':
                hedgehogs.append((i, j))
    
    while True:
        count += 1
        hedgehogs = move_hedgehogs(hedgehogs)
        if not hedgehogs:
            break
        waters = water_expand(waters)
    if hedgehogs is None:
        print(count)
    else:
        print("KAKTUS")
        
if __name__ == "__main__":
    main()