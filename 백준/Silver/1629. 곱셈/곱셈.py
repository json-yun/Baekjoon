import sys

A, B, C = [int(a) for a in sys.stdin.readline().split()]

def main() -> None:
    # A = A * B + r (0 <= r < B, r은 자연수)
    # A = x * y (x, y는 자연수) 일 때
    # A = (x * B + r_x) * (y * B + r_y)
    # A = (x * y * B * B) + (x * r_y * B) + (y * r_x * B) + (r_x * r_y)
    # A = (xyB+xr_y+yr_x)*B + r_x*r_y 이므로
    # r_x * r_y = z * B + r 을 만족하는 자연수 z가 존재한다.
    def _find_remainder(A :int, B :int, C :int) -> int:
        B_half = B//2
        if B_half in cache:
            left = cache[B_half]
        else:
            left = _find_remainder(A, B_half, C)
        if B-B_half in cache:
            right = cache[B-B_half]
        else:
            right = _find_remainder(A, B-B_half, C)
        quotient = (left*right)%C
        cache[B] = quotient
        return quotient
    cache = {0: 1,
             1: A%C}
    cache = {i: _find_remainder(A, i, C) for i in range(1000)}
    print(_find_remainder(A, B, C))

main()