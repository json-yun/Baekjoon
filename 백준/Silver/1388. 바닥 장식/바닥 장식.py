import sys

input = sys.stdin.readline

def main() -> None:
    def check_v(map: list[list[str]]) -> int:
        cnt = 0
        for j in range(M):
            last = ""
            for i in range(N):
                if last != '|' and map[i][j] == '|':
                    cnt += 1
                last = map[i][j]
        return cnt
    def check_h(map: list[str]) -> int:
        cnt = 0
        for i in range(N):
            last = ""
            for j in range(M):
                if last != '-' and map[i][j] == '-':
                    cnt += 1
                last = map[i][j]
        return cnt
    
    N, M = map(int, input().split())
    A = [input().rstrip() for _ in range(N)]

    print(check_h(A) + check_v(A))

if __name__ == "__main__":
    main()