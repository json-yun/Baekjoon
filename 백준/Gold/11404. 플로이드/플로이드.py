import sys
input = sys.stdin.readline
INF = 10000001

def main() -> None:
    N = int(input())
    M = int(input())
    adj: list[list] = [[INF]*(N) for _ in range(N)]
    for i in range(N):
        adj[i][i] = 0
        
    for _ in range(M):
        i, j, cost = map(int, input().split())
        i -= 1
        j -= 1
        adj[i][j] = min(adj[i][j], cost)

    for k in range(N): # stopover
        for i in range(N): # departure
            for j in range(N): # arrival
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])

    for r in adj:
        print(*(i if i != INF else 0 for i in r))
    
if __name__ == "__main__":
    sys.exit(main())