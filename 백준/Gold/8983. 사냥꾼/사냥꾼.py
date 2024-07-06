import sys

def main():
    M, N, L = [int(i) for i in sys.stdin.readline().split()]
    LANE = [int(i) for i in sys.stdin.readline().split()]
    ANIMALS = [tuple(map(int, sys.stdin.readline().split())) for i in range(N)]

    MIN_X, MAX_X = [max(0, min(LANE)-L), min(1_000_000_000, max(LANE)+L)]
    MAX_Y = L
    ANIMALS = [(x-y, x+y) for x, y in ANIMALS if all((y<=MAX_Y, MIN_X<=x<=MAX_X))]

    LANE.sort()
    ANIMALS.sort()

    answer = 0
    for h in LANE:
        lb, rb = h-L, h+L
        checked = []
        for i, a in enumerate(ANIMALS):
            if lb <= a[0]:
                if a[1] <= rb:
                    answer += 1
                    checked.append(i)
                elif rb < a[0]:
                    break
            else:
                checked.append(i)
        for c in sorted(checked, reverse=True):
            ANIMALS.pop(c)
    print(answer)

main()