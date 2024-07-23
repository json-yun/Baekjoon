A = input().rstrip().split('-')
B = []
for a in A:
    B.append(sum(map(int, a.split('+'))))
result = B[0]
for i in range(1, len(B)):
    result -= B[i]
print(result)