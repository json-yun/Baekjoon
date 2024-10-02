import sys
from collections import deque
input = sys.stdin.readline

def main() -> None:
    N, P = map(int, input().split())
    stack = [[0] for _ in range(7)]

    cnt = 0
    for _ in range(N):
        i, p = map(int, input().split())
        while stack[i][-1] > p:
            stack[i].pop()
            cnt += 1
        if stack[i][-1] < p:
            stack[i].append(p)
            cnt += 1

    print(cnt)
    
if __name__ == "__main__":
    sys.exit(main())