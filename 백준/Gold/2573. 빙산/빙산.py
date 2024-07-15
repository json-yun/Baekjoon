import sys
from collections import deque

input = sys.stdin.readline

def main() -> None:
    def melt():
        def check_4way(i: int, j: int) -> int:
            result = 0
            if (i-1, j) not in ices:
                result += 1
            if (i, j-1) not in ices:
                result += 1
            if (i+1, j) not in ices:
                result += 1
            if (i, j+1) not in ices:
                result += 1
            return result
        items_pop = []
        for idx, h in ices.items():
            h -= check_4way(*idx)
            if h <= 0:
                items_pop.append(idx)
            else:
                ices[idx] = h
        for idx in items_pop:
            ices.pop(idx)
    # 하나의 덩어리이면 True
    def check_unity() -> bool:
        ices_ = ices.copy()
        q = deque()
        q.append(ices_.popitem()[0])
        while q:
            i, j = q.popleft()
            if (idx:=(i-1, j)) in ices_:
                ices_.pop(idx)
                q.append(idx)
            if (idx:=(i, j-1)) in ices_:
                ices_.pop(idx)
                q.append(idx)
            if (idx:=(i+1, j)) in ices_:
                ices_.pop(idx)
                q.append(idx)
            if (idx:=(i, j+1)) in ices_:
                ices_.pop(idx)
                q.append(idx)
        return not bool(ices_)
    N, M = map(int, input().split())
    # A = []
    ices = {}
    for i in range(N):
        temp = []
        for j, h in enumerate(map(int, input().split())):
            temp.append((i, j))
            if h > 0:
                ices[(i, j)] = h
        # A.append(temp)
    time = 1
    melt()
    while ices:
        if not check_unity():
            print(time)
            return
        time += 1
        melt()
    print(0)
    
main()