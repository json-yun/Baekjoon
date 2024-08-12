def solution(game_board, table):
    di = (1, 0, 0, -1)
    dj = (0, 1, -1, 0)
    def bfs(table, find = 1):
        N = len(table)
        table = [row[:] for row in table]
        puzzles = []
        for i in range(N):
            for j in range(N):
                if table[i][j] == find:
                    q = [(i, j)]
                    idx = 0
                    while len(q) >= idx+1:
                        table[i][j] = 0 if find else 1
                        cur = q[idx]
                        idx += 1
                        for d in range(4):
                            if 0 <= cur[0]+di[d] < N and 0 <= cur[1]+dj[d] < N and table[cur[0]+di[d]][cur[1]+dj[d]] == find:
                                table[cur[0]+di[d]][cur[1]+dj[d]] = 0 if find else 1
                                q.append((cur[0]+di[d], cur[1]+dj[d]))
                    puzzles.append(q)
                    
        return puzzles

    def normalize(puzzle):
        di, dj = min(puzzle, key=lambda x: x[0])[0], min(puzzle, key=lambda x: x[1])[1]
        new_puzzle = []
        
        for i, j in puzzle:
            new_puzzle.append((i-di, j-dj))
        new_puzzle.sort()
        
        return new_puzzle

    def rotate(table):
        N = len(table)
        new_table = [[0]*N for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                new_table[i][j] = table[N-j-1][i]

        return new_table
    
    answer = 0
    
    places = [[normalize(p), 1] for p in bfs(game_board, 0)]
    
    for _ in range(4):
        for puzzle in bfs(table):
            puzzle_n = normalize(puzzle)
            for i in range(len(places)):
                place, o = places[i]
                if o and place == puzzle_n:
                    for p in puzzle:
                        table[p[0]][p[1]] = 0
                    answer += len(puzzle)
                    places[i][1] = 0
                    break
        table = rotate(table)
    
    return answer