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
                s, m, e = j, j+k-1, j+i-1
                if c[s][e] > (m:=c[s][m] + c[m+1][e] + A[j][0]*A[m][1]*A[e][1]):
                    c[s][e] = m
                    
    print(c[0][N-1])

if __name__ == "__main__":
    main()