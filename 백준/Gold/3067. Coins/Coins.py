import sys

input = sys.stdin.readline

def main() -> None:
    def check_cases(target: int, type_idx: int) -> int:
        if (target, type_idx) in cache:
            return cache[(target, type_idx)]
        result = 0
        coin_value = COIN_TYPE[type_idx]
        
        if type_idx >= N:
            return 0
        elif type_idx == N-1:
            return int(target%coin_value==0)
        for i in range(target//coin_value, -1, -1):
            residual = target - coin_value * i
            if residual == 0:
                result += 1
            elif COIN_TYPE[-1] <= residual:
                result += check_cases(residual, type_idx+1)

        cache[(target, type_idx)] = result
        return result
    
    CASES = int(input())
    for _ in range(CASES):
        cache = {}
        N = int(input())
        COIN_TYPE = [int(i) for i in input().split()[::-1]]
        TARGET = int(input())
        print(check_cases(TARGET, 0))
    
if __name__ == "__main__":
    main()