import sys
import random

class str_(str):
    def __init__(self, l :str) -> None:
        super().__init__()
        # self.len = len(str)
    
    def __lt__(self, other) -> bool:
        l_self = len(self)
        l_other = len(other)
        if l_self == l_other:
            for i in range(l_self):
                if self[i] == other[i]:
                    continue
                else:
                    return self[i] < other[i]
            return False
        else:
            return l_self < l_other
    
    def __rt__(self, other) -> bool:
        l_self = len(self)
        l_other = len(other)
        if l_self == l_other:
            for i in range(l_self):
                if self[i] == other[i]:
                    continue
                else:
                    return self[i] > other[i]
            return False
        else:
            return l_self > l_other
        
    def __eq__(self, other) -> bool:
        l_self = len(self)
        l_other = len(other)
        if l_self == l_other:
            for i in range(l_self):
                if self[i] == other[i]:
                    continue
                else:
                    return False
            return True
        else:
            return False
        

N = int(input())
numbers = [str(sys.stdin.readline().rstrip()) for _ in range(N)]
numbers = [str_(i) for i in numbers]

def arg_median(*args :str_) -> int:
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
        
    # input()
    if idx_l < end:
        quick_sort(numbers, idx_l, end)
    if idx_r > start:
        quick_sort(numbers, start, idx_r)

def del_duplicated(numbers):
    i = 0
    while i < len(numbers)-1:
        while numbers[i] == numbers[i+1]:
            numbers.pop(i)
            i -= 1
            break
        i += 1

quick_sort(numbers, 0, N-1)
del_duplicated(numbers)
for i in numbers:
    print(i)