import sys

input = sys.stdin.readline

def main():
    N = int(input())
    # m_to_d = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # m_to_d = [sum(m_to_d[:i]) for i in range(13)]
    m_to_d = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    flowers = []
    for _ in range(N):
        m1, d1, m2, d2 = map(int, input().split())
        flowers.append((m_to_d[m1]+d1, m_to_d[m2]+d2))
    flowers.sort()

    curr = m_to_d[3]+1 # 3월 1일 시작
    temp = 0
    cnt = 0
    i = 0
    while curr < m_to_d[12]+1: # 12월 1일 이후로 지는 꽃이 있어야 함
        if i < len(flowers) and flowers[i][0] <= curr:
            temp = max(temp, flowers[i][1])
            i += 1
        else:
            if temp == 0:
                cnt = 0
                break
            curr = temp
            temp = 0
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()