def solution(numbers, target):
    answer = 0
    n = len(numbers)-1
    def _dfs(total, i):
        if abs(total-target) > abs(sum(numbers[i:])):
            return
        number = numbers[i]
        if i == n:
            if total + number == target or total - number == target:
                nonlocal answer
                answer += 1
            else: 
                return
        else:
            _dfs(total+number, i+1)
            _dfs(total-number, i+1)
    numbers.sort(reverse=True)
    _dfs(0, 0)
    
    return answer