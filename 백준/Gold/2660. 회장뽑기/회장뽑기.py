import sys
input = sys.stdin.readline
INF = 51

def main() -> None:
    N = int(input())
    adj = [[INF]*(N) for _ in range(N)]
    for i in range(N):
        adj[i][i] = 0
        
    while (edge:=[*map(int, input().split())]) != [-1, -1]:
        i, j = edge
        i -= 1
        j -= 1
        adj[i][j] = 1
        adj[j][i] = 1

    for k in range(N): # stopover
        for i in range(N): # departure
            for j in range(N): # arrival
                adj[i][j] = min(adj[i][j], adj[i][k]+adj[k][j])

    min_value = INF
    chairs = []
    for i, candidate in enumerate(adj):
        if (cand_value:=max(candidate)) < min_value:
            min_value = cand_value
            chairs = []
            chairs.append(i)
        elif cand_value == min_value:
            chairs.append(i)
            
    print(min_value, len(chairs))
    print(*(i+1 for i in chairs))
    
if __name__ == "__main__":
    sys.exit(main())