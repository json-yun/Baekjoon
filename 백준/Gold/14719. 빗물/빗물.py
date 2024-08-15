def main() -> None:
    H, W = map(int, input().split())
    WALL = list(map(int, input().split()))

    answer = 0
    idx_max = 0
    for i in range(1, W):
        if WALL[i] > WALL[i-1]:
            for j in range(i-1, idx_max, -1):
                if WALL[j] >= WALL[i]:
                    break
                answer += min(WALL[idx_max], WALL[i])-WALL[j]
                WALL[j] = min(WALL[idx_max], WALL[i])
            if WALL[i] >= WALL[idx_max]:
                idx_max = i

    print(answer)

main()