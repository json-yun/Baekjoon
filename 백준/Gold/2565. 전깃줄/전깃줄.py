import sys
input = sys.stdin.readline

def main() -> None:
    N = int(input())
    A = []
    for _ in range(N):
        f, t = input().split()
        A.append((int(f), int(t)))

    A.sort()
    dp = [1]*N

    for i in range(N-1):
        for j in range(i+1, N):
            if A[i][1] < A[j][1]:
                dp[j] = max(dp[j], dp[i] + 1)

    print(N-max(dp))

if __name__ == "__main__":
    sys.exit(main())