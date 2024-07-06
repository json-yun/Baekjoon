import sys
from collections import defaultdict

def main():
    def bin_search(l, r, start, end):
        if start >= end:
            return False
        mid = (end+start)//2
        if LANE[mid] < l:
            return bin_search(l, r, mid+1, end)
        elif r < LANE[mid]:
            return bin_search(l, r, start, mid)
        else:
            return True

    M, N, L = [int(i) for i in sys.stdin.readline().split()]
    LANE = [int(i) for i in sys.stdin.readline().split()]
    ANIMALS = [tuple(map(int, sys.stdin.readline().split())) for i in range(N)]

    MIN_X, MAX_X = [max(0, min(LANE)-L), min(1_000_000_000, max(LANE)+L)]
    MAX_Y = L
    animals = defaultdict(list)
    for x, y in ANIMALS:
        if all((y<=MAX_Y, MIN_X<=x<=MAX_X)):
            animals[y].append(x)
    LANE.sort()

    answer = 0
    for y, xs in animals.items():
        for x in xs:
            if bin_search(x-(L-y), x+(L-y), 0, M):
                answer += 1
    print(answer)

main()