import sys
from collections import deque
import heapq

input = sys.stdin.readline
INF = 100000001

def main() -> None:
    def dijkstra(start, end) -> None:
        cost_list = [None] + [INF] * N
        visited = [None] + [False] * N
        priority_q = [(0, start)]
        cost_list[start] = 0
        now = start
        while now != end:
            now = heapq.heappop(priority_q)[1]
            if visited[now] == True:
                continue
            visited[now] = True
            for to in buses[now]:
                if not visited[to]:
                    new_cost = cost_list[now]+buses[now][to]
                    if new_cost < cost_list[to]:
                        cost_list[to] = new_cost
                        heapq.heappush(priority_q, (new_cost, to))
        print(cost_list[end])
    
    N = int(input())
    M = int(input())
    buses = {i: {} for i in range(1, N+1)}
    for i in range(M):
        frm, to, cost = map(int, input().split())
        buses[frm][to] = cost if to not in buses[frm] else min(cost, buses[frm][to])
    start, end = map(int, input().split())
    
    dijkstra(start, end)
    
main()