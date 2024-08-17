def main() -> None:
    INF = 25000001
    def BF() -> bool:
        dist_shortest = [INF for _ in range(N+1)]
        
        dist_shortest[roads[0][0]] = 0
        for _ in range(N-1):
            for s, e, t in roads:
                if dist_shortest[s] + t < dist_shortest[e]:
                    dist_shortest[e] = dist_shortest[s] + t

        for s, e, t in roads:
            if dist_shortest[s] + t < dist_shortest[e]:
                return True

        return False
    
    TC = int(input())

    for _ in range(TC):
        N, M, W = map(int, input().split())

        roads = []
        for _ in range(M):
            s, e, t = map(int, input().split())
            roads.append((s, e, t))
            roads.append((e, s, t))

        for _ in range(W):
            s, e, t = map(int, input().split())
            roads.append((s, e, -t))

        if BF():
            print("YES")
        else:
            print("NO")

main()
