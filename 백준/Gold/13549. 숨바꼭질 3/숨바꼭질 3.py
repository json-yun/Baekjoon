from collections import deque

def main() -> None:
    N, K = map(int, input().split())
    # N, K = 5, 17
    cost = [100000] * 100001

    q = deque()

    q.append(N)
    cost[N] = 0
    while len(q):
        cur = q.popleft()
        if cur == K:
            break

        i = cur
        while 0 < i <= 100000:
            if cost[i] > cost[cur]:
                q.appendleft(i)
                cost[i] = cost[cur]
            i *= 2
        if cur+1 <= 100000 and cost[cur+1] >= 100000:
            q.append(cur+1)
            cost[cur+1] = cost[cur] + 1
        if cur-1 >= 0 and cost[cur-1] >= 100000:
            q.append(cur-1)
            cost[cur-1] = cost[cur] + 1

    print(cost[K])

    
main()
