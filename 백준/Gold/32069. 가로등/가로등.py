import sys
input = sys.stdin.readline

def main() -> None:
    # L: L까지, N: 가로등 수, K: 출력할 수
    L, N, K = map(int, input().split())
    LIGHTS = [*map(int, input().split())]
    lights_l = {i: True for i in LIGHTS}
    lights_r = {i: True for i in LIGHTS}

    i = 0
    visited = {}
    # 0 처리
    while i < K and i < N:
        print(0)
        visited[LIGHTS[i]] = True
        i += 1

    dist = 1
    while i < K:
        for l in LIGHTS:
            if lights_l[l]:
                if i >= K:
                    break
                if lights_l.get(l-dist, False) or l-dist < 0 or visited.get(l-dist):
                    lights_l[l] = False
                else:
                    i += 1
                    print(dist)
                    visited[l-dist] = True

            if lights_r[l]:
                if i >= K:
                    break
                if lights_r.get(l+dist, False) or l+dist > L or visited.get(l+dist):
                    lights_r[l] = False
                else:
                    i += 1
                    print(dist)
                    visited[l+dist] = True
        dist += 1

if __name__ == "__main__":
    sys.exit(main())