from itertools import combinations

def main():
    def distance(a: tuple, b: tuple) -> int:
        a1, a2 = a
        b1, b2 = b

        return abs(a1-b1)  + abs(a2-b2)

    def sum_min(*args) -> int:
        combi = list(args)
        minimum = 10000000
        
        for case in combi:
            result = []
            for i in range(len(homes)):
                temp = 101
                for dist in case:
                    if dist[i] < temp:
                        temp = dist[i]
                result.append(temp)
            
            minimum = min(sum(result), minimum)

        return minimum
    
    N, M = map(int, input().split())
    homes = []
    chickens = []
    for i in range(N):
        for j, m in enumerate(map(int, input().split())):
            if m == 1:
                homes.append((i, j))
            elif m == 2:
                chickens.append((i, j))

    chicken_dist = []
    for chicken in chickens:
        chicken_dist.append([])
        for home in homes:
            chicken_dist[-1].append(distance(chicken, home))

    print(sum_min(*combinations(chicken_dist, M)))

main()