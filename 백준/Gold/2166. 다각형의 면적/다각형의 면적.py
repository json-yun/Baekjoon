import sys
input = sys.stdin.readline

def cross_product(vectors: list[tuple]) -> float:
    inner = 0
    outer = 0
    x_0, y_0 = vectors[-1]
    for x, y in vectors:
        inner += x_0 * y
        outer += y_0 * x
        x_0 = x
        y_0 = y

    return abs(inner-outer)/2

N = int(input())
poly = [tuple(map(int, input().split())) for _ in range(N)]
area = cross_product(poly)

print(f"{area:.1f}")