A=[sum(int(i) for i in a.split('+')) for a in input().strip().split('-')]
print(2*A[0]-sum(A))