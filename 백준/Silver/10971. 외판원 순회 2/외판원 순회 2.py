import sys

N = int(sys.stdin.readline())
MIN = 1000000 * (N+1) + 1
cost_table = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]

# O(n!)
def TSP(now :int, to_visit_list :list, cost_now :int):
    global MIN
    def _visit(to):
        cost_to = cost_table[now][to]
        if cost_to:
            return cost_now + cost_to
        else:
            return 0
    
    if not to_visit_list:
        if cost_table[now][0]!= 0:
            cost = _visit(0)
            MIN = min(cost, MIN)
    
    # 모든 곳을 방문 했다면 첫 위치로 이동
    # 아니라면 다음 위치로 이동
    for to_visit in to_visit_list:
        cost = _visit(to_visit)
        if cost and cost < MIN:
            new_to_visit_list = to_visit_list[:]
            new_to_visit_list.remove(to_visit)
            TSP(to_visit, new_to_visit_list, cost)

TSP(0, list(range(1, N)), 0)
print(MIN)
