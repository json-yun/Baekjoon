import sys

N = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

def bubble_sort_plus(numbers :list[int], start :int) -> None:
    if start >= N-1:
        return
    
    indicator = 0
    for i in range(N-1, start, -1):
        indicator += 1
        if numbers[i-1] > numbers[i]:
            temp = numbers[i]
            numbers[i] = numbers[i-1]
            numbers[i-1] = temp
            indicator = 0
    
    if indicator == N-start-1:
        return
    bubble_sort_plus(numbers, start+1+indicator)

bubble_sort_plus(numbers, 0)
for i in numbers:
    print(i)