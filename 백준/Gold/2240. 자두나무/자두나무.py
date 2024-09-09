import sys

input = sys.stdin.readline

def main() -> None:
    T, W = map(int, input().split())
    plums = [int(input()) for _ in range(T)]
    
    # dp[i][j] : i번째 시간에 j번 이동했을 때 받을 수 있는 최대 자두 수
    dp = [[0] * (W + 1) for _ in range(T + 1)]
    
    for i in range(1, T + 1):
        for j in range(W + 1):
            # 현재 자두가 떨어지는 나무 번호
            current_tree = plums[i - 1]
            
            # 나무를 바꾸지 않는 경우
            dp[i][j] = dp[i - 1][j] + (1 if (current_tree == 1 and j % 2 == 0) or (current_tree == 2 and j % 2 == 1) else 0)
            
            # 나무를 바꾸는 경우
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + (1 if (current_tree == 1 and j % 2 == 0) or (current_tree == 2 and j % 2 == 1) else 0))
    
    # 최대 자두 수 계산
    result = max(dp[T])
    print(result)

if __name__ == "__main__":
    sys.exit(main())