import sys

input = sys.stdin.readline

def main():
    N = int(input())
    month_to_date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_to_date = [sum(month_to_date[:i]) for i in range(13)]

    flowers = []
    for _ in range(N):
        m1, d1, m2, d2 = map(int, input().split())
        flowers.append((month_to_date[m1]+d1, month_to_date[m2]+d2))
    # 60-334

    flowers.sort(key=lambda x: (x[0], x[1]))

    curr = 60
    temp = 0
    cnt = 0
    i = 0
    while curr <= 334:
        if i < len(flowers) and flowers[i][0] <= curr and temp <= 334:
            if flowers[i][1] > temp:
                temp = flowers[i][1]
            i += 1
        else:
            if temp:
                curr = temp
                temp = 0
                cnt += 1
            else:
                cnt = 0
                break

    print(cnt)

if __name__ == "__main__":
    main()