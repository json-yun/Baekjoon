N = int(input())

board = [list(input().split()) for _ in range(N)]
bishop = [False]*(2*N-1) # i-j+N-1
                
def dfs(level, highest, count):
    if (2*N-1-level)+count <= highest:
        return 0
    result = max(highest, count)

    flag = True
    for i in range(max(0, level-(N-1)), min(N, level+1)):
        j = level-i
        if board[i][j] == '0' or bishop[i-j+N-1]:
            continue
        flag = False
        bishop[i-j+N-1] = True
        if (new:=dfs(level+1, result, count+1)) > result:
            result = new
        bishop[i-j+N-1] = False

    if flag and (new:=dfs(level+1, result, count)) > result:
        result = new
        
    return result

print(dfs(0, 0, 0))