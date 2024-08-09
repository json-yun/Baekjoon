# 최단 경로가 아니라
# 최소 비용을 들여 다리를 건설하는 문제이므로
# 현재 이어진 섬에서 최소 비용으로 연결하는 다리를 선택하면
# 최적해의 일부해가 된다!
    
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    
    f, t, c = costs.pop(0)
    visited = [f, t]
    answer = c
    print(visited)
    while (len(visited) < n):
        for f, t, c in costs:
            if f in visited and t in visited:
                continue
            if f not in visited and t not in visited:
                continue
            if t not in visited:
                visited.append(t)
            elif f not in visited:
                visited.append(f)
            answer += c
            break
    
    return answer