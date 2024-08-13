INF = 100

def solution(maze):
    def get_blue_flag(i, j):
        return maze[i][j]//100
    
    def get_red_flag(i, j):
        return maze[i][j]%100//10
    
    def find_start():
        red = blue = 0
        for i in range(N):
            for j in range(M):
                if maze[i][j] == 1:
                    maze[i][j] = 0
                    red = (i, j)
                elif maze[i][j] == 2:
                    maze[i][j] = 0
                    blue = (i, j)
            if red and blue:
                break
            
        return red, blue

    def possible_way(pos, is_blue, flag):
        if flag: return [pos]
        i, j = pos
        get_flag = get_blue_flag if is_blue else get_red_flag
        ways = []
        if i < N-1 and maze[i+1][j]%10 != 5 and get_flag(i+1, j) != 1:
            ways.append((i+1, j))
        if j < M-1 and maze[i][j+1]%10 != 5 and get_flag(i, j+1) != 1:
            ways.append((i, j+1))
        if i > 0 and maze[i-1][j]%10 != 5 and get_flag(i-1, j) != 1:
            ways.append((i-1, j))
        if j > 0 and maze[i][j-1]%10 != 5 and get_flag(i, j-1) != 1:
            ways.append((i, j-1))

        return ways

    def move_wagon(red, blue, cnt, red_flag, blue_flag):
        nonlocal answer
        if cnt >= answer:
            return
        
        if not red_flag:
            maze[red[0]][red[1]] += 10
            if maze[red[0]][red[1]] % 10 == 3:
                red_flag = True
                
        if not blue_flag:
            maze[blue[0]][blue[1]] += 100
            if maze[blue[0]][blue[1]] % 10 == 4:
                blue_flag = True
        
        if red_flag and blue_flag:
            answer = cnt
            
        for new_red in possible_way(red, 0, red_flag):
            for new_blue in possible_way(blue, 1, blue_flag):
                # 교차 방지
                if new_red == blue and new_blue == red:
                    continue
                # 중복 방지
                if new_red == new_blue:
                    continue
                move_wagon(new_red, new_blue, cnt+1, red_flag, blue_flag)

        maze[red[0]][red[1]] -= 10
        maze[blue[0]][blue[1]] -= 100

    N = len(maze)
    M = len(maze[0])
    answer = INF
    move_wagon(*find_start(), 0, False, False)
    
    return answer if answer != INF else 0