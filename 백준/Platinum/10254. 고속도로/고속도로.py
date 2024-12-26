import sys

input = sys.stdin.readline

def ccw(pos) -> float:
    y, x = pos
    if x == Px:
        return 0
    elif y == Py:
        return -float('inf')
    else:
        return -(x-Px)/(y-Py)

def cross_product(v1, v2):
    x1, y1 = v1
    x2, y2 = v2

    return x1*y2 - y1*x2

def distance_squared(v1, v2):
    x1, y1 = v1
    x2, y2 = v2

    return (x1-x2)**2 + (y1-y2)**2

def candidates(q):
    l = len(q)
    for i in range(l):
        v0, v1 = q[i], q[(i+1)%l]
        v1_0 = v1[0]-v0[0], v1[1]-v0[1]

        j = i+bin_search(v1_0, i, q)
        v2 = q[j%l]
        v3 = q[(j+1)%l]
        v4 = q[(j+2)%l]
        v5 = q[(j-1)%l]
        v3_0 = v3[0]-v2[0], v3[1]-v2[1]
        if cross_product(v1_0, v3_0) == 0:
            yield ((v0, v2), (v0, v3), (v0, v4), (v0, v5), (v1, v2), (v1, v3), (v1, v4), (v1, v5))
        else:
            yield ((v0, v2), (v0, v3), (v0, v4), (v1, v2), (v1, v3), (v1, v4))

def bin_search(v0, i, q):
    l = len(q)
    lo, hi = 1, l

    while lo+1 < hi:
        mid = (lo+hi) // 2
        v2 = q[(i+mid)%l]
        v3 = q[(i+mid+1)%l]
        v3_0 = v3[0]-v2[0], v3[1]-v2[1]
        if cross_product(v0, v3_0) <= 0:
            lo = mid
        else:
            hi = mid

    return lo
    
T = int(input())
for _ in range(T):
    N = int(input())
    dots = [tuple(map(int, input().split())) for _ in range(N)]
    # import random
    # dots = [(random.randrange(-100000, 100000), random.randrange(-100000, 100000)) for _ in range(N)]
    # dots = [(-939, -707), (-769, 794), (556, -74), (981, -236), (187, -507), (602, -741), (381, -737), (-124, -792), (344, -855), (-678, -873)]
    # dots = [(-96001, -19383),(-94809, 55470), (-93327, 93794), (-74828, 82354), (-63109, 80916), (-30010, 89553), (-35125, 77221), (-25705, 88657), (-38385, 57379), (-27644, 63832), (-5873, 86556), (5100, 87865), (15037, 90289), (-18184, 55027), (-3043, 69300), (-69039, 3844), (-49494, 14837), (33458, 75683), (72043, 94434), (72112, 88264), (-30125, 20233), (-48911, 6685), (38958, 54918), (53473, 45296), (34423, 21895), (28114, 19709), (-46427, -9013), (99238, 8936), (84964, -7201), (50822, -14720), (97580, -32160), (76627, -32545), (41905, -42829), (46552, -45902), (80148, -75884), (50454, -67472), (-3730, -51989), (5115, -58196), (54363, -77477), (58950, -88779), (-56082, -39351), (-50494, -45631), (-7970, -83336), (-7182, -93769), (-44502, -89980), (-69917, -73971), (-68052, -83162), (-94304, -25215), (-81103, -73077), (-92740, -37999)]
    # dots = [(-49, -10), (-46, 85), (-45, 94), (-2, 99), (90, 49), (91, -20), (89, -34), (69, -86)]

    Py, Px = dots.pop(dots.index(min(dots)))
    dots.sort(key=ccw)

    # from collections import deque
    # from itertools import combinations
    # q = deque()
    # q.append((Py, Px))
    # for dot in dots:
    #     if len(q) < 2:
    #         q.append(dot)
    #         continue
    #     while True:
    #         y0, x0 = q[-2]
    #         y1, x1 = q[-1]
    #         y2, x2 = dot
    #         if cross_product((x1-x0, y1-y0), (x2-x0, y2-y0)) > 0:
    #             q.append(dot)
    #             break
    #         else:
    #             q.pop()

    # max_dist = 0
    # max_arg = ()
    # for v in combinations(q, 2):
    #     if max_dist < (dist:=distance_squared(*v)):
    #         max_dist = dist
    #         max_arg = (*v[0], *v[1])

    # tt = max_dist
    # ttt = max_arg

    # Graham Scan
    q = []
    q.append((Py, Px))
    for dot in dots:
        while True:
            if len(q) < 2:
                q.append(dot)
                break
            y0, x0 = q[-2]
            y1, x1 = q[-1]
            y2, x2 = dot
            if (cp:=cross_product((x1-x0, y1-y0), (x2-x0, y2-y0))) > 0:
                q.append(dot)
                break
            elif cp == 0 and (x0<x2<x1 or y0<y2<y1):
                break
            else:
                q.pop()

    # rotating calipers
    max_dist = 0
    max_arg = ()
    for vs in candidates(q):
        for v in vs:
            if max_dist < (dist:=distance_squared(*v)):
                max_dist = dist
                max_arg = (*v[0], *v[1])

    print(*max_arg)
    # if max_dist != tt:
    #     print(ttt, tt)
    #     print(max_arg, max_dist)
    #     print(q)
    