import sys
import time

input = sys.stdin.readline

### 입력
N = int(input())
A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
def main():
    AB = []
    CD = {}
    for c in C:
        for d in D:
            if (cd := c + d) in CD:
                CD[cd] += 1
            else:
                CD[cd] = 1

    result = 0
    for a in A:
        for b in B:
            if (ab := -(a + b)) in CD:
                result += CD[ab]

    print(result)

main()