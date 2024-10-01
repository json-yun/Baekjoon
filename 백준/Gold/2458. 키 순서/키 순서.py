import sys
input = sys.stdin.readline

def main() -> None:
    N, M = map(int, input().split())
    adj = [[0]*N for _ in range(N)]
    for _ in range(M):
        s, e = map(int, input().split())
        adj[s-1][e-1] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if adj[i][k] and adj[k][j]:
                    adj[i][j] = 1

    cnt = 0
    for i in range(N):
        sum_conn = sum(adj[i])
        for j in range(N):
            sum_conn += adj[j][i]
        if sum_conn == N-1:
            cnt += 1
    
    print(cnt)
    
if __name__ == "__main__":
    sys.exit(main())