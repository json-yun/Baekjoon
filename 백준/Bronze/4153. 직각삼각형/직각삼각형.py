while True:
    A = list(map(int, input().split()))
    if any(a==0 for a in A):
        break
    total = 0
    total += A.pop(A.index(min(A)))**2
    total += A.pop(A.index(min(A)))**2
    if total==(A[0]**2):
        print("right")
    else:
        print("wrong")