import sys
input = sys.stdin.readline

# 지도 한 변 크기 N
N = int(input())
apt = [[] for _ in range(N)]
for i in range(N):
    buildings = input().strip()
    for building in buildings:
        apt[i].append(building)


# 지도 순회 돌리면서
# visitied에 체크 안돼있으면 dfs 시작
# dfs 돌면서 visitied에 체크 싹 다 때린 후에
# dfs 끝나면 cnt += 1

visitied = [[] for _ in range(N)] 
for i in range(N):
    for j in range(N):
        visitied[i].append('0')

def dfs(i,j):
    global cnt
    cnt += 1
    visitied[i][j] = '1'
    di = [1,-1,0,0]
    dj = [0,0,1,-1]

    for k in range(4):
        i_udlr, j_udlr = i+di[k], j+dj[k]
        if 0 <= i_udlr < N and 0 <= j_udlr < N:
            if apt[i_udlr][j_udlr] == '1':
                if visitied[i_udlr][j_udlr] == '0':
                    visitied[i_udlr][j_udlr] = '1'
                    dfs(i_udlr,j_udlr)
    return cnt

cnt_list = []
total_group = 0

for i in range(N):
    for j in range(N):
        if apt[i][j] == '1' and visitied[i][j] == '0':
            cnt = 0
            total_group += 1
            cnt_list.append(dfs(i,j))

print(total_group)
cnt_list.sort()
for cnt in cnt_list:
    print(cnt)
