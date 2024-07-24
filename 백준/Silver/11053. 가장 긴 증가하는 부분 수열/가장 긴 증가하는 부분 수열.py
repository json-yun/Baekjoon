import sys

input = sys.stdin.readline

def main() -> None:
    N = int(input())
    A = [int(i) for i in input().split()]
    arr = [1]*N

    result = 1
    for i in range(N):
        for j in range(i+1):
            if A[j] < A[i] and arr[i] < (e:=arr[j]+1):
                arr[i] = e
        if result < arr[i]:
            result = arr[i]

    print(result)
    
if __name__ == "__main__":
    main()