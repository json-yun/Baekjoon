def main() -> None:
    N, K = map(int, input().split())
    ITEMS: list[tuple[int, int]] = [tuple(map(int, input().split())) for _ in range(N)]
    ITEMS.sort()
    ITEMS = [None] + ITEMS
    arr = [[0 for _ in range(K+1)]] + [[0] for _ in range(N)]

    for n in range(1, N+1):
        for k in range(1, K+1):
            if (w:=ITEMS[n][0]) <= k:
                arr[n].append(max(arr[n-1][k], arr[n-1][k-w] + ITEMS[n][1]))
            else:
                arr[n].append(arr[n-1][k])

    print(arr[N][K])

if __name__ == "__main__":
    main()