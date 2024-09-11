import sys
from itertools import combinations

input = sys.stdin.readline

def main() -> None:
    def dfs(cur_i, cur_j):
        nonlocal min_delta
        if sum(visited) > N//2:
            return False
        if sum(visited) == N//2:
            min_delta = min(min_delta, resi())
            return True
        
        for i in range(cur_i, N//2):
            visited[i] = True
            for j in range(max(cur_j, i+1), N):
                if sum(visited) > N//2:
                    break
                if not(visited[i] and visited[j]):
                    visited[j] = True
                    print(i, j)
                    dfs(i, j)
                    visited[j] = False
            visited[i] = False

    def resi() -> int:
        score1 = 0
        score2 = 0
        for key, value in V.items():
            if visited[key[0]]:
                if visited[key[1]]:
                    score1 += value
            else:
                if not visited[key[1]]:
                    score2 += value
                
        return abs(score1 - score2)
    
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    V: dict[tuple, int] = {}
    for i in range(N):
        for j in range(i+1, N):
            V[(i, j)] = matrix[i][j] + matrix[j][i]

    min_delta = 2001
    for combi in combinations(range(N), N//2):
        visited = [False] * N
        for c in combi:
            visited[c] = True
        min_delta = min(min_delta, resi())

    print(min_delta)

if __name__ == "__main__":
    sys.exit(main())