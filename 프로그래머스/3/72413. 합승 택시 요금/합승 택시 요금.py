INF = 1000001

def solution(n, s, a, b, fares):
    fares_d = {}
    a -= 1
    b -= 1
    s -= 1
    for x, y, f in fares:
        x -= 1
        y -= 1
        if x not in fares_d:
            fares_d[x] = {}
        if y not in fares_d:
            fares_d[y] = {}
        fares_d[x][y] = f
        fares_d[y][x] = f
    print(fares_d)

    def dijkstra(start):
        is_visited = [0 for _ in range(n)]
        distance = [INF for _ in range(n)]
        def visit(i):
            is_visited[i] = 1
            try:
                visitables = fares_d[i]
            except KeyError:
                return
            visited = []
            for node, fare in visitables.items():
                if is_visited[node]:
                    continue
                distance[node] = min(distance[node], fare+distance[i])
                visited.append((node, distance[node]))
        
        distance[start] = 0
        s = start
        while True:
            visit(s)
            if 0 not in is_visited:
                break
            closest = [y if x == 0 and y > 0 else INF for x, y in zip(is_visited, distance)]
            s = closest.index(min(closest)) if min(closest) != INF else is_visited.index(0)
        return distance
    
    cost_a = dijkstra(a)
    cost_b = dijkstra(b)
    cost_s = dijkstra(s)
    return min([a+b+s for a, b, s in zip(cost_a, cost_b, cost_s)])

def solution(n, s, a, b, fares):
    fares_d = {}
    a -= 1
    b -= 1
    s -= 1
    for x, y, f in fares:
        x -= 1
        y -= 1
        if x not in fares_d:
            fares_d[x] = {}
        if y not in fares_d:
            fares_d[y] = {}
        fares_d[x][y] = f
        fares_d[y][x] = f

    def dijkstra(start):
        is_visited = [0 for _ in range(n)]
        distance = [INF for _ in range(n)]
        def visit(i):
            is_visited[i] = 1
            try:
                visitables = fares_d[i]
            except KeyError:
                return
            visited = []
            for node, fare in visitables.items():
                if is_visited[node]:
                    continue
                distance[node] = min(distance[node], fare+distance[i])
                visited.append((node, distance[node]))
        
        distance[start] = 0
        s = start
        while True:
            visit(s)
            if 0 not in is_visited:
                break
            closest = [y if x == 0 and y > 0 else INF for x, y in zip(is_visited, distance)]
            s = closest.index(min(closest)) if min(closest) < INF else is_visited.index(0)
        return distance
    
    cost_a = dijkstra(a)
    cost_b = dijkstra(b)
    cost_s = dijkstra(s)
    return min([a+b+s for a, b, s in zip(cost_a, cost_b, cost_s)])