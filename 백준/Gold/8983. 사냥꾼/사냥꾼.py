import sys

M, N, L = [int(i) for i in sys.stdin.readline().split()]
LANE = [int(i) for i in sys.stdin.readline().split()]
ANIMALS = [tuple(map(int, sys.stdin.readline().split())) for i in range(N)]
# M, N, L = [4, 8, 4]
# LANE = [6, 1, 4, 9]
# ANIMALS = [(7, 2), (3, 3), (4, 5), (5, 1), (2, 2), (1, 4), (8, 4), (9, 4)]
# M, N, L = [1, 5, 3]
# LANE = [3]
# ANIMALS = [(2, 2), (1, 1), (5, 1), (4, 2), (3, 3)]

MIN_X, MAX_X = [max(0, min(LANE)-L), min(1_000_000_000, max(LANE)+L)]
MAX_Y = L
ANIMALS = [(animal[0]-animal[1], animal[0]+animal[1]) for animal in ANIMALS if all((animal[1]<=MAX_Y, MIN_X<=animal[0]<=MAX_X))]

LANE.sort()
ANIMALS.sort()
# print(LANE)
# print(ANIMALS)

answer = 0
for h in LANE:
    lb, rb = h-L, h+L
    checked = []
    for i, a in enumerate(ANIMALS):
        if rb < a[0]:
            break
        elif lb <= a[0] and a[1] <= rb:
            answer += 1
            checked.append(i)
        elif a[0] < lb:
            checked.append(i)
    for c in sorted(checked, reverse=True):
        ANIMALS.pop(c)
print(answer)
            