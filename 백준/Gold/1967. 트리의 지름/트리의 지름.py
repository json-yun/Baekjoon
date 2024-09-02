import sys
from itertools import combinations

input = sys.stdin.readline

def main():
    N = int(input())
    childs = [{}] + [{} for _ in range(N)]
    parents = [0] + [0 for _ in range(N)]
    level = [0]*(N+1)

    tree_height = 0
    for i in range(1, N):
        p, c, w = map(int, input().split())
        childs[p][c] = w
        parents[c] = p
        level[c] = level[p] + 1
        tree_height = tree_height if tree_height >= level[c] else level[c]

    level_dict = [[] for _ in range(tree_height+1)]
    for i in range(1, N+1):
        level_dict[level[i]].append(i)
        
    for q in reversed(level_dict):
        for i in q:
            if len(childs[i]) > 2:
                a = sorted(childs[i].items(), key=lambda x: -x[1])[:2]
                childs[i] = dict(a)
                
            max_w = 0
            for w in childs[i].values():
                if w > max_w:
                    max_w = w

            if i != 1:
                childs[parents[i]][i] += max_w

    max_l = 0
    for v in childs:
        if (v:=sum(v.values())) > max_l:
            max_l = v
            
    print(max_l)

if __name__ == "__main__":
    main()