import sys
from collections import deque

input = sys.stdin.readline

def main() -> None:
    def check_4way(i: int, j: int) -> list[tuple[int, int]]:
        di = (1, 0, 0, -1)
        dj = (0, 1, -1, 0)
        result = []
        
        for d in range(4):
            curr_i, curr_j = i+di[d], j+dj[d]
            if 0<=curr_i<N and 0<=curr_j<N and A[curr_i][curr_j] == '1':
                A[curr_i][curr_j] = '0'
                result.append((curr_i, curr_j))
    
        return result
    
    def count_home(i: int, j: int) -> int:
        q = deque()
        q.append((i, j))
        cnt = 0
        A[i][j] = '0'
        
        while q:
            curr_i, curr_j = q.popleft()
            cnt += 1
            for next in check_4way(curr_i, curr_j):
                q.append(next)
                
        return cnt
    
    def find_new_home() -> tuple[int, int] | None:
        for i in range(N):
            for j in range(N):
                if A[i][j] == '1':
                    return (i, j)
                
        return None
    
    N = int(input())
    A = [list(input().rstrip()) for _ in range(N)]

    cnt = 0
    cnt_n_home = []
    while next:=find_new_home():
        cnt += 1
        cnt_n_home.append(count_home(*next))
    
    cnt_n_home.sort()
    print(cnt)
    print(*cnt_n_home, sep="\n")

if __name__ == "__main__":
    main()