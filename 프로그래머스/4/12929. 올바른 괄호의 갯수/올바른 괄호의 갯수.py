def solution(n):
    answer = 0
    result = [1, 1]
    
    for i in range(2, n+1):
        result.append(0)
        for j in range(i+1):
            result[-1] += result[j-1] * result[i-j]
    
    answer = result[-1]
    return answer

# ()

# ()1개
# (1개)

# (0개) 2개       2
# (1개) 1개     1
# (2개) 0개     2


# (0개) 3개       5
# (2개) 1개     2
# (1개) 2개     2
# (3개) 0개     5