import sys

input = sys.stdin.readline

def main():
    N, C = map(int, input().split())
    home = []
    bot, top = 1000000000, 0
    for _ in range(N):
        r = int(input())
        home.append(r)
        bot = min(bot, r)
        top = max(top, r)
    home.sort()
    interval = (top-bot+1)//(C-1) + 1
    bot = 0
    top = interval + 1
    max_success_interval = 0

    while bot != interval and top != interval:
        c = C
        last = home[0]
        c -= 1
        for h in home:
            if h-last >= interval:
                c -= 1
                last = h
            if c == 0:
                break
        else:
            # 실패 시 간격 감소
            top = interval
            interval = (bot+interval) //2
            continue
        # 성공 시 간격 증가
        max_success_interval = max(max_success_interval, interval)
        bot = interval
        interval = (interval+top) //2

    print(max_success_interval)

if __name__ == "__main__":
    main()