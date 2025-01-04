import sys

board = [list(map(int, [*input()])) for _ in range(9)]

hor = [[None]+[False]*9 for _ in range(9)]
ver = [[None]+[False]*9 for _ in range(9)]
squ = [[None]+[False]*9 for _ in range(9)]
void = []
for i in range(9):
    for j in range(9):
        if (n:=board[i][j]) != 0:
            hor[i][n] = True
            ver[j][n] = True
            squ[i//3*3+j//3][n] = True
        else:
            void.append((i, j))

def dfs(level: int):
    if level == len(void):
        print(*(''.join(map(str, row)) for row in board), sep="\n")
        sys.exit()
    i, j = void[level]
    for n in range(1, 10):
        if hor[i][n] == False and ver[j][n] == False and squ[i//3*3+j//3][n] == False:
            hor[i][n] = True
            ver[j][n] = True
            squ[i//3*3+j//3][n] = True
            board[i][j] = n
            dfs(level+1)
            hor[i][n] = False
            ver[j][n] = False
            squ[i//3*3+j//3][n] = False

dfs(0)