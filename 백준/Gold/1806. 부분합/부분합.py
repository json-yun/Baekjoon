N, S = map(int, input().split())
A = list(map(int, input().split()))

# 왼쪽 포인터 a, 오른쪽 포인터 b
a = b = 0
total = sum(A[a:b+1])
shortest = N+1

# b가 N-1까지 진행한다.
# 즉, 오른쪽 끝이 0에서 N-1까지인 각각의 경우에서 조건을 만족하는 가장 짧은 수열을 찾는다.
while b < N:
    # 합계가 조건을 만족하는 경우에만 a를 오른쪽으로 옮긴다.
    # 자연수 수열이므로, a를 옮기면 합계(total)는 감소한다.
    # 현재 조건을 만족하지 않는 경우 a를 증가시켜도 조건을 만족하지 않으므로 탐색할 필요가 없다.
    if total >= S:
        shortest = min(shortest, b-a+1)
        total -= A[a]
        a += 1
    elif b < N-1:
        b += 1
        total += A[b]
    else:
        break

print(shortest if shortest < N+1 else 0)