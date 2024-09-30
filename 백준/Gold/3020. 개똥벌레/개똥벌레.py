import sys
import test
input = sys.stdin.readline

def main() -> None:
    N, H = map(int, input().split())
    
    cone, icicle = {}, {}
    for _ in range(N//2):
        h = int(input())
        cone[h] = cone.get(h, 0) + 1
        h = int(input())
        icicle[H-h] = icicle.get(H-h, 0) + 1

    total = N//2
    min_wall = N//2
    count = 0
    for i in range(H):
        total -= cone.get(i, 0) - icicle.get(i, 0)
        if total < min_wall:
            min_wall = total
            count = 1
        elif total == min_wall:
            count += 1

    print(min_wall, count)
    
if __name__ == "__main__":
    sys.exit(main())