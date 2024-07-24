import sys
input = sys.stdin.readline
def main() -> None:
    CASES = int(input())
    
    for _ in range(CASES):
        N = int(input()) # 지원자
        P = [list(map(int, input().split())) for _ in range(N)]
        P.sort()

        m = 100001
        result = 0
        for i in range(N):
            if P[i][1] < m:
                m = P[i][1]
                result += 1
            elif m == 1:
                break
        
        print(result)

if __name__ == "__main__":
    main()