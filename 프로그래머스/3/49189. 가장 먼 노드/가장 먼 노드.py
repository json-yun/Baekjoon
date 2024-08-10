from collections import deque


def solution(n, edge):
    answer = 0
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    edges = {i: [] for i in range(1, n+1)}
    for i, j in edge:
        edges[i].append(j)
        edges[j].append(i)
        
    q = deque()
    q.append((1, 0))
    steps = 0
    max_d = 0
    while len(q):
        cur, steps = q.popleft()
        if steps > max_d:
            answer = 1
            max_d = steps
        elif steps == max_d:
            answer += 1
        
        for e in edges[cur]:
            if not visited[e]:
                visited[e] = 1
                q.append((e, steps+1))
        
    return answer