from collections import deque

N = int(input())
E = [0]+[int(input()) for _ in range(N)]
visited = [0]*(N+1)

result = 0
result_list = []
for i in range(1, N+1):
    if visited[i]:
        continue
        
    cnt = 1
    start = i
    visited[start] = 1
    next = E[start]
    temp_visited = visited[:]
    temp_list = [next]
    while not visited[next]:
        visited[next] = 1
        next = E[next]
        cnt += 1
        temp_list.append(next)
    if next == start:
        result += cnt
        result_list.extend(temp_list)
    else:
        visited = temp_visited

print(result)
result_list.sort()
print(*result_list, sep="\n")