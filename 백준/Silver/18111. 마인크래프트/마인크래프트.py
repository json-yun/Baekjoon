import sys
input = sys.stdin.readline

def main() -> None:
    def count_block(target_h: int) -> tuple[int]:
        block_need = 0
        block_get = 0
        for row in CHUNK:
            for point in row:
                delta_block = point-target_h
                if delta_block > 0:
                    block_get += delta_block
                else:
                    block_need -= delta_block

        return block_get, block_need

    def _calc_time(block_get, block_need) -> int | None:
        if B+block_get >= block_need:
            return block_get*2 + block_need
        return float('inf')

    def calc_time(target_h: int) -> int | None:
        return _calc_time(*count_block(target_h))

    N, M, B = map(int, input().split())
    CHUNK = []
    btm, top = 256, 0
    for _ in range(N):
        CHUNK.append([*map(int, input().split())])
        btm = min(btm, min(CHUNK[-1]))
        top = max(top, max(CHUNK[-1]))
    
    time_btm = calc_time(btm)
    time_top = calc_time(top)
    mid = (btm+top+1)//2
    time_mid = calc_time(mid)
    while True:
        mid_l, mid_r = (btm+mid)//2, (mid+top)//2
        time_mid_l, time_mid_r = calc_time(mid_l), calc_time(mid_r)
        
        minimum = min(time_mid_l, time_mid, time_mid_r)
        # 조건문 순서가 중요
        if minimum == time_mid_r:
            if (btm, mid, top) == (mid, mid_r, top):
                break
            btm, mid, top = mid, mid_r, top
            time_btm, time_mid, time_top = time_mid, time_mid_r, time_top
        elif minimum == time_mid:
            if (btm, mid, top) == (mid_l, mid, mid_r):
                break
            btm, mid, top = mid_l, mid, mid_r
            time_btm, time_mid, time_top = time_mid_l, time_mid, time_mid_r
        else:
            if (btm, mid, top) == (btm, mid_l, mid):
                break
            btm, mid, top = btm, mid_l, mid
            time_btm, time_mid, time_top = time_btm, time_mid_l, time_mid

    if time_mid < time_top:
        print(time_mid, mid)
    else:
        print(time_top, top)

if __name__ == "__main__":
    sys.exit(main())
