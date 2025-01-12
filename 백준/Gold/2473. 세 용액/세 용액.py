N = int(input())

solution = list(map(int, input().split()))
solution.sort()

def bin_search(target, frm):
    btm, top = frm, N-1

    while btm+1 < top:
        mid = (btm+top) // 2
        if solution[mid] > target:
            top = mid
        elif solution[mid] == target:
            return mid
        else:
            btm = mid

    if abs(target-solution[btm]) < abs(target-solution[top]):
        return btm
    else:
        return top

ground_1 = bin_search(0, 0) # 0이상 중 가장 작은 수의 인덱스

rev = False
if ground_1 > N//2:
    solution = [-x for x in reversed(solution)]
    rev = True
    ground_1 = N-1-ground_1
    
if solution[ground_1] < 0:
    if ground_1 < N-1:
        ground_1 += 1

result_v = 3000000000
result = (solution[0], solution[1], solution[2])
for i in range(N-2):
    for j in range(i+1, N-1):
        subtotal = solution[i]+solution[j]
        if subtotal < 0:
            if subtotal+solution[j+1] > result_v:
                break
            k = bin_search(-subtotal, max(j+1, ground_1-1))
            if (total:=abs(subtotal+solution[k])) < result_v:
                result_v = total
                result = (solution[i], solution[j], solution[k])
                if result_v == 0:
                    break
        else:
            k = j + 1
            if (total:=abs(subtotal+solution[k])) < result_v:
                result_v = total
                result = (solution[i], solution[j], solution[k])
            break
    if result_v == 0:
        break

if rev:
    print(*(-x for x in reversed(result)))
else:
    print(*result)