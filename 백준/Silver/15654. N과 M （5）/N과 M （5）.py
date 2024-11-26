def permutation(start: int, n: int)->list:
    if n < 1: return []
    result = []

    if n > 1:
        for i in range(N):
            if visited[i]: continue
            visited[i] = True
            result.extend([[nums[i]]+t for t in permutation(i+1, n-1)])
            visited[i] = False
    else:
        for i in range(N):
            if visited[i]: continue
            visited[i] = True
            result.append([nums[i]])
            visited[i] = False

    return result

N, M = map(int, input().split())
nums = list(map(int, input().split()))
visited = [False] * N
nums.sort()
for perm in permutation(0, M):
    print(*perm)