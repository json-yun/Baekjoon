def main():
    N = int(input())

    oo = ol = 1
    for _ in range(N-1):
        oo, ol = oo+ol+ol, oo+ol

    print(sum([oo, ol*2])%9901)

main()