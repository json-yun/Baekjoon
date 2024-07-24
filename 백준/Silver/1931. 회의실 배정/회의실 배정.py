import sys

input = sys.stdin.readline

def main() -> None:
    N = int(input())
    A = [tuple(map(int, input().split())) for _ in range(N)]
    A.sort(key=lambda x: (x[1], x[0]))
    
    f = 0
    result = 0
    for a in A:
        if a[0]>=f:
            f = a[1]
            result += 1
            
    print(result)

if __name__ == "__main__":
    main()