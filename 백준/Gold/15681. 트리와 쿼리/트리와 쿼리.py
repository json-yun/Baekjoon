import sys

sys.setrecursionlimit(200000)
input = sys.stdin.readline

def main():
    def dfs(n, p):
        result = 1
        for child in childs[n]:
            if child != p:
                result += dfs(child, n)
        
        cache[n] = result
        return result
    
    N, R, Q = map(int, input().split())

    childs = {i: [] for i in range(1, N+1)}
    for _ in range(N-1):
        p, c = map(int, input().split())
        childs[p].append(c)
        childs[c].append(p)
        
    cache = {}

    dfs(R, 0)

    for _ in range(Q):
        print(cache[int(input())])

if __name__ == "__main__":
    main()