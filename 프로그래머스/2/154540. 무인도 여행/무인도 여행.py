def solution(maps):
    answer = []
    queue = []
    maps = [list(x) for x in maps]
    N = len(maps)
    M = len(maps[0])
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X':
                queue.append((i, j))
                answer.append(0)
                while queue:
                    x, y = queue.pop()
                    if maps[x][y] != 'X':
                        answer[-1] += int(maps[x][y])
                        maps[x][y] = 'X'
                    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        queue.append((x+dx, y+dy)) if 0 <= x+dx < N and 0 <= y+dy < M and maps[x+dx][y+dy] != 'X' else None
    
    answer.sort()
    if not answer:
        answer = [-1]
    return answer