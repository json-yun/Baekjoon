import sys

A, B, C = [int(a) for a in sys.stdin.readline().split()]

def main() -> None:
    def _find_remainder(A, B, C):
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
        return quotient
    cache = {0: 1,
             1: A%C}
    cache = {i: _find_remainder(A, i, C) for i in range(1000)}
    print(_find_remainder(A, B, C))

main()