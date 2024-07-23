import sys
input = sys.stdin.readline
INF = 2**31
def main() -> None:
    N = int(input())
    A = [tuple(map(int, input().split())) for _ in range(N)]
    c = [[INF if i != j else 0 for j in range(N)] for i in range(N)]
    for i in range(2, N+1): # 길이-1
        for j in range(0, N-i+1): # 위치
            for k in range(1, i):
                if c[j][j+i-1] > (m:=c[j][j+k-1] + c[j+k][j+i-1] + A[j][0]*A[j+k][0]*A[j+i-1][-1]):
                    c[j][j+i-1] = m
    # print(*c, sep="\n")
    print(c[0][N-1])
    
main()