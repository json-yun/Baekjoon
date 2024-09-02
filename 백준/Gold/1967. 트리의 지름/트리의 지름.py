import sys
from itertools import combinations

input = sys.stdin.readline

def main():
    N = int(input())
    # is_leaf = [0] + [1]*(N)
    childs = [{}] + [{} for _ in range(N)]
    parents = [None] + [None for _ in range(N)]
    level = [0]*(N+1)

    max_level = 0
    for i in range(1, N):
        p, c, w = map(int, input().split())
        childs[p][c] = w
        parents[c] = p
        level[c] = level[p] + 1
        max_level = max(max_level, level[c])

    while max_level >= 0:
        q = [i for i in range(1, N+1) if level[i] == max_level]
        max_level -= 1
        
        for i in q:
            if parents[i] is None:
                break
                
            max_w = 0
            for w in childs[i].values():
                max_w = max(max_w, w)
            childs[parents[i]][i] += max_w

    max_l = 0
    for v in childs:
        vs = list(v.values())
        vs.sort(reverse=True)
        max_l = max(max_l, sum(vs[:2]))
            
    print(max_l)

if __name__ == "__main__":
    main()