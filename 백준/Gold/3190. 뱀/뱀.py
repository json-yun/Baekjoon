import sys

# 보드 크기
N = 6
N = int(sys.stdin.readline())
# 사과 수
M = 3
M = int(sys.stdin.readline())
APPLES = [(3, 4), (2, 5), (5, 3)]
APPLES = [map(int, sys.stdin.readline().split()) for _ in range(M)]
# 방향전환 횟수
L = 3
L = int(sys.stdin.readline())
TURNS = [(3, 'D'), (15, 'L'), (17, 'D')]
TURNS = [sys.stdin.readline().split() for _ in range(L)]

############# 사과 인덱스는 0부터인가 1부터인가
APPLES = [(x-1, y-1) for x, y in APPLES]
APPLES_ROW = {i: [] for i in range(N)}
APPLES_COL = {i: [] for i in range(N)}
APPLES.sort()
for x, y in APPLES:
    APPLES_ROW[x].append(y)
APPLES.sort(key=lambda x: (x[1], x[0]))
for x, y in APPLES:
    APPLES_COL[y].append(x)

class Snake:
    def __init__(self) -> None:
        self.snake = [0, 0]
        self.head = 0   # 0: right, 1: down, 2: left, 3: up
        self.board = [[0]*N for _ in range(N)]
        self.length = 1
        self.board[0][0] = self.length
        self.elapsed = 0
    
    # 회전시킨다.
    def turn(self, direction: str) -> None:
        if direction == 'D':
            self.head = (self.head+1) % 4
        elif direction == 'L':
            self.head = (self.head-1) % 4
    
    # 충돌 거리를 반환하는 함수
    def _collision(self, seconds: int) -> int | None:
        # 벽체크
        if self.head == 0: # 오른쪽
            for s, d in enumerate(range(self.snake[1]+1, self.snake[1]+1+seconds), 1):
                # 벽을 만나거나 몸통을 만나면
                if d >= N or self.board[self.snake[0]][d]-s >= 0:
                    return s
        elif self.head == 2: # 왼쪽
            for s, d in enumerate(range(self.snake[1]-1, self.snake[1]-1-seconds, -1), 1):
                if d < 0 or self.board[self.snake[0]][d]-s >= 0:
                    return s
        elif self.head == 1: # 아래
            for s, d in enumerate(range(self.snake[0]+1, self.snake[0]+1+seconds), 1):
                if d >= N or self.board[d][self.snake[1]]-s >= 0:
                    return s
        elif self.head == 3: # 위
            for s, d in enumerate(range(self.snake[0]-1, self.snake[0]-1-seconds, -1), 1):
                if d < 0 or self.board[d][self.snake[1]]-s >= 0:
                    return s
        return None
    
    # 현재 방향으로 최대seconds만큼 이동
    # 사과를 발견하면 멈추고 사과를 먹는다.
    # 몸통 또는 벽에 충돌하면 멈춘다.
    # 진행한 시간만큼 elapsed를 늘려줘야 한다.
    def move(self, seconds: int) -> tuple[int] | None:
        # 경로와 거리 안에 벽/몸통이 있는가?
        # 있으면 충돌
        # 경로와 이동거리 안에 사과가 있는가?
        # 없으면 이동한다.
        # 1 벽에 충돌
        # 2 몸에 충돌
        # 사과로 몸 늘어남
        def _move(cells: int, apple: int=0) -> int | None:
            self._timepass(cells-apple)
            self.elapsed += cells
            if self.head == 0:
                # 몸통 마킹
                # l: 몸통값, d: 좌표(x)
                for l, d in enumerate(range(self.snake[1]+1, self.snake[1]+1+cells), self.length-cells+1):
                    self.board[self.snake[0]][d] = max(0, l)
                self.snake[1] += cells
            elif self.head == 2:
                for l, d in enumerate(range(self.snake[1]-1, self.snake[1]-1-cells, -1), self.length-cells+1):
                    self.board[self.snake[0]][d] = max(0, l)
                self.snake[1] -= cells
            elif self.head == 1:
                for l, d in enumerate(range(self.snake[0]+1, self.snake[0]+1+cells), self.length-cells+1):
                    self.board[d][self.snake[1]] = max(0, l)
                self.snake[0] += cells
            elif self.head == 3:
                for l, d in enumerate(range(self.snake[0]-1, self.snake[0]-1-cells, -1), self.length-cells+1):
                    self.board[d][self.snake[1]] = max(0, l)
                self.snake[0] -= cells
        
        while seconds != 0:
            # 사과 체크
            near_wall = self._collision(seconds)
            near_apple = self._apples_in(near_wall if near_wall else seconds)
            
            # 사과가 있으면 사과를 먹고 사과 자리로 이동
            if near_apple:
                self.length += 1
                _move(near_apple, 1)
                APPLES_ROW[self.snake[0]].remove(self.snake[1])
                APPLES_COL[self.snake[1]].remove(self.snake[0])
                seconds -= near_apple
            # 사과가 없으면 충돌을 판별하고 충돌이 아니라면 이동
            else:
                if near_wall is None:
                    _move(seconds)
                    seconds = 0
                else:
                    self.elapsed += near_wall
                    return self.elapsed
        return None
    
    # 사과가 있으면 가장 가까운 거리를, 없으면 None
    # 사과를 없애지는 않으니 주의
    def _apples_in(self, seconds: int) -> int | None:
        if self.head == 0: # 오른쪽
            for apple in APPLES_ROW[self.snake[0]]:
                if self.snake[1] < apple < self.snake[1]+seconds+1:
                    return abs(apple - self.snake[1])
        elif self.head == 2: # 왼쪽
            for apple in reversed(APPLES_ROW[self.snake[0]]):
                if self.snake[1]-seconds-1 < apple < self.snake[1]:
                    return abs(apple - self.snake[1])
        elif self.head == 1: # 아래
            for apple in APPLES_COL[self.snake[1]]:
                if self.snake[0] < apple < self.snake[0]+seconds+1:
                    return abs(apple - self.snake[0])
        elif self.head == 3: # 위
            for apple in reversed(APPLES_COL[self.snake[1]]):
                if self.snake[0]-seconds-1 < apple < self.snake[0]:
                    return abs(apple - self.snake[0])
        return None
    
    # 뱀 몸통의 시간초를 seconds만큼 줄임
    def _timepass(self, seconds: int) -> None:
        def __timepass(e: int) -> int:
            return max(0, e-seconds)
        for i in range(N):
            self.board[i] = list(map(__timepass, self.board[i]))

snake = Snake()
crashed = False
for time, dir in TURNS:
    if endat:=snake.move(int(time)-snake.elapsed):
        crashed = True
        break
    snake.turn(dir)
if not crashed:
    snake.move(N)
print(snake.elapsed)