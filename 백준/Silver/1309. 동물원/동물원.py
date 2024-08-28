def main():
    N = int(input())

    oo = 1
    ol = 1
    lo = 1
    for _ in range(N-1):
        oo, ol, lo = oo+ol+lo, oo+lo, lo+oo

    print(sum([oo, ol, lo])%9901)

main()