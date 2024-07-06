import sys
sys.setrecursionlimit(100000)

N = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

def arg_median(*args :int) -> int:
    temp = []
    for i in range(3):
        if args[(i+1)%3] > args[i]:
            if (i+1)%3 in temp:
                temp.remove((i+1)%3)
            else:
                temp.append((i+1)%3)
        else:
            if i in temp:
                temp.remove(i)
            else:
                temp.append(i)
    return temp[0]

def quick_sort(
    numbers: list[int], 
    start :int, 
    end :int) -> None:
    if start == end:
        return
    idx_l = start
    idx_r = end
    pivot = (start+end)//2
    # 피봇 선택
    pivot_cand = {0: idx_l, 1: pivot, 2: idx_r}
    med = arg_median(numbers[idx_l], numbers[pivot], numbers[idx_r])
    pivot = pivot_cand[med]
    
    n_pivot = numbers[pivot]
    while idx_l <= idx_r:
        while numbers[idx_l] < n_pivot:
            idx_l += 1
        while n_pivot < numbers[idx_r]:
            idx_r -= 1
        if idx_l > idx_r:
            break
        numbers[idx_l], numbers[idx_r] = numbers[idx_r], numbers[idx_l]
        idx_r -= 1
        idx_l += 1
        
    if idx_l < end:
        quick_sort(numbers, idx_l, end)
    if idx_r > start:
        quick_sort(numbers, start, idx_r)


quick_sort(numbers, 0, N-1)
for i in numbers:
    print(i)