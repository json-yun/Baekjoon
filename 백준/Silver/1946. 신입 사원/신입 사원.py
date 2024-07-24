def main() -> None:
    CASES = int(input())
    
    for _ in range(CASES):
        N = int(input()) # 지원자
        P = [tuple(map(int, input().split())) for _ in range(N)]
        P.sort()

        m = 100001
        for _, p in P:
            if p < m:
                m = p
            else:
                N -= 1
        
        print(N)

if __name__ == "__main__":
    main()