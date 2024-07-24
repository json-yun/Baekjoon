import sys

input = sys.stdin.readline

def main() -> None:
    N = int(input())
    A = [int(i) for i in input().split()]
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        arr[i][i] = 1

    result = 1
    for i in range(N):
        for j in range(i+1):
            for k in range(i-1, j-1, -1):
                if A[k] < A[i]:
                    if arr[i][j] < (e:=arr[k][j]+1):
                        arr[i][j] = e
                if result < arr[i][j]:
                    result = arr[i][j]

    print(result)
    
if __name__ == "__main__":
    main()