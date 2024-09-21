import sys
input = sys.stdin.readline

def main() -> None:
    def drive(idx, curr, cost):
        nonlocal answer
        for i in range(idx, len(roads)):
            s, e, dist = roads[i]
            if curr <= s:
                idx_old, curr_old, cost_old = idx, curr, cost

                cost += s-curr
                cost += dist
                curr = e
                idx = i+1
            else:
                drive(i, curr_old, cost_old)

        cost += L-curr

        answer = min(answer, cost)
                

    N, L = map(int, input().split())
    roads = []
    for _ in range(N):
        s, e, dist = map(int, input().split())
        if e-s <= dist:
            continue
        if e > L:
            continue

        roads.append((s, e, dist))

    roads.sort(key=lambda x: (x[0], -x[1]))
    # print(roads)
    answer = L
    drive(0, 0, 0)
    print(answer)

if __name__ == "__main__":
    sys.exit(main())