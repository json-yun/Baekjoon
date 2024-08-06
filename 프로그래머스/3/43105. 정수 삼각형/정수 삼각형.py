def solution(triangle):
    answer = 0
    N = len(triangle)
    totals = [[0 for j in range(i)] for i in range(1, N+1)]
    totals[0][0] = triangle[0][0]
    for r in range(N-1):
        for c in range(r+2):
            if c <= 0:
                totals[r+1][c] = triangle[r+1][c] + totals[r][c]
            elif c >= r+1:
                totals[r+1][c] = triangle[r+1][c] + totals[r][c-1]
            else:
                totals[r+1][c] = triangle[r+1][c] + max(totals[r][c], totals[r][c-1])
    answer = max(totals[-1])
    # print(*totals, sep="\n")
    return answer