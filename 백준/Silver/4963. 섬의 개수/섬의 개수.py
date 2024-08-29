from collections import deque

def is_exterior(i, j, MAP):
    if not (0 <= i < len(MAP)):
        return True
    if not (0 <= j < len(MAP[0])):
        return True
    return False

def dfs(i, j, MAP):
    q = deque()

    result = 0
    q.append((i, j))
    while q:
        i, j = q.popleft()
        if is_exterior(i, j, MAP):
            continue
        if MAP[i][j] == 0:
            continue

        MAP[i][j] = 0
        result = 1
        q.append((i, j+1))
        q.append((i, j-1))
        q.append((i+1, j))
        q.append((i-1, j))
        q.append((i-1, j-1))
        q.append((i-1, j+1))
        q.append((i+1, j+1))
        q.append((i+1, j-1))
    
    return result

def main():
    while (size := input().split()) != ['0', '0']:
        w, h = map(int, size)
        MAP = []
        for _ in range(h):
            MAP.append([int(i) for i in input().split()])
        
        result = 0
        for i in range(len(MAP)):
            for j in range(len(MAP[0])):
                result += dfs(i, j, MAP)
        
        print(result)

main()