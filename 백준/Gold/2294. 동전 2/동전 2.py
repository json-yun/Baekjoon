import sys

input = sys.stdin.readline

def main() -> None:
    def check_cases(target: int, type_idx: int, n_coins: int) -> bool:
        if type_idx >= N:
            return False
        elif type_idx == N-1:
            return all((target//COIN_TYPE[type_idx] <= n_coins, target%COIN_TYPE[type_idx]==0))
        # if (target, type_idx, n_coins) in cache:
        #     return cache[(target, type_idx, n_coins)]
        for i in range(min(target//COIN_TYPE[type_idx], n_coins), -1, -1):
            # 맞아 떨어지면
            if (residual:=target - COIN_TYPE[type_idx] * i) == 0:
                # cache[(target, type_idx, n_coins)] = True
                return True
            elif COIN_TYPE[-1] <= residual <= COIN_TYPE[type_idx+1]*(n_coins-i) :
                if check_cases(residual, type_idx+1, n_coins-i):
                    # cache[(target, type_idx, n_coins)] = True
                    return True
        # cache[(target, type_idx, n_coins)] = False
        return False
    # cache = {}
    N, K = map(int, input().split())
    COIN_TYPE = []
    for _ in range(N):
        c = int(input())
        if c not in COIN_TYPE:
            COIN_TYPE.append(c)
    COIN_TYPE.sort(reverse=True)
    N = len(COIN_TYPE)
    for i in range(1, K//COIN_TYPE[-1]+1):
        if check_cases(K, 0, i):
            print(i)
            return
    print(-1)
    
if __name__ == "__main__":
    main()