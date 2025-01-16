from collections import defaultdict

def ccw(v0, v1, v2):
    x0, y0 = v0
    x1, y1 = v1
    x2, y2 = v2

    return (x1-x0)*(y2-y0) - (x2-x0)*(y1-y0)

def dot_on_line(dot, line):
    x0, y0, x1, y1 = line
    x, y = dot

    return min(x0, x1) <= x <= max(x0, x1) and min(y0, y1) <= y <= max(y0, y1)

def intersection(l1, l2):
    x1, y1, x2, y2 = l1
    x3, y3, x4, y4 = l2
    
    v1, v2, v3, v4 = (x1, y1), (x2, y2), (x3, y3), (x4, y4)

    ccw1 = ccw(v1, v2, v3) * ccw(v1, v2, v4)
    ccw2 = ccw(v3, v4, v1) * ccw(v3, v4, v2)

    if ccw1 <= 0 and ccw2 <= 0:
        if ccw1 < 0 or ccw2 < 0:
            return True
        if dot_on_line(v3, v1+v2) or dot_on_line(v4, v1+v2) or dot_on_line(v1, v3+v4) or dot_on_line(v2, v3+v4):
            return True
                
    return False

def find_parent(i):
    if parents[i] != i:
        parents[i] = find_parent(parents[i])
        
    return parents[i]

N = int(input())
lines = []
for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append((x1, y1, x2, y2) if x1 <= x2 else (x2, y2, x1, y1))
    
lines.sort()

parents = [i for i in range(N)]
for i in range(N):
    for j in range(i):
        if lines[j][2] < lines[i][0]:
            continue
        if intersection(lines[i], lines[j]):
            p_i = find_parent(i)
            p_j = find_parent(j)
            parents[max(p_i, p_j)] = min(p_i, p_j)

groups = defaultdict(int)
for i in range(N):
    groups[find_parent(i)] += 1

print(len(groups))
print(max(groups.values()))