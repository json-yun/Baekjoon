T = int(input())
for _ in range(T):
    N = int(input())
    board = []
    board.append(tuple(map(int, input().split())))
    board.append(tuple(map(int, input().split())))

    points = [0, 0, 0] # 위/아래/안 뗐을 경우

    for i in range(N):
        points = [max(points[1], points[2]) + board[0][i],
                  max(points[0], points[2]) + board[1][i],
                  max(points[0], points[1])]

    print(max(points))