import sys

input = sys.stdin.readline

def main() -> None:
    S, C = map(int, input().split())
    pas = []
    total_pa = 0
    length = 1000000000
    for _ in range(S):
        pa = int(input())
        total_pa += pa
        # length = min(length, pa)
        pas.append(pa)

    length = total_pa//(C-1)
    bot, top = -1, length+1

    while bot != length and top != length:
        chicken_w_pa = 0
        for pa in pas:
            chicken_w_pa += pa//length
            if chicken_w_pa >= C:
                break
        else:
            top = length
            length = (bot+length)//2
            continue
        remaind_pa = total_pa - C * length
        bot = length
        length = (length+top)//2

    print(remaind_pa)

if __name__ == "__main__":
    sys.exit(main())