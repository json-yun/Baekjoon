A=[sum(map(int,a.split('+')))for a in input().split('-')]
print(2*A[0]-sum(A))