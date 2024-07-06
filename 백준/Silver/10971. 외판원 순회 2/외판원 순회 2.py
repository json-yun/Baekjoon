import sys

N = int(sys.stdin.readline().strip())
MIN = 1000000 * (N+1) + 1
cost_table = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]

# O(n!)
def TSP(now: int, to_visit_flag: list, cost_now: int):
    global MIN
    
    if all(not visit for visit in to_visit_flag):
        # 모든 곳을 방문 했다면 첫 위치로 이동
        cost = cost_now + cost_table[now][0]
        if cost_table[now][0] != 0:  # 경로가 존재할 경우에만
            MIN = min(cost, MIN)
        return
    
    for to_visit in range(1, N):
        if to_visit_flag[to_visit] and cost_table[now][to_visit] != 0:
            to_visit_flag[to_visit] = False
            TSP(to_visit, to_visit_flag, cost_now + cost_table[now][to_visit])
            to_visit_flag[to_visit] = True

TSP(0, [i != 0 for i in range(N)], 0)
print(MIN)
