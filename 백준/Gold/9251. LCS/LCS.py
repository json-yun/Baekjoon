import sys

input = sys.stdin.readline

def main() -> None:
    A = input().rstrip()
    B = input().rstrip()
    N_A = len(A)
    N_B = len(B)
    arr = [[0]*(N_B+1) for _ in range(N_A+1)]

    for i in range(1, N_A+1):
        for j in range(1, N_B+1):
            if A[i-1] == B[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
            elif arr[i-1][j] >= arr[i][j-1]:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = arr[i][j-1]

    print(arr[N_A][N_B])

if __name__ == "__main__":
    main()