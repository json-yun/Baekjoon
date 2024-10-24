import sys
from collections import deque
input = sys.stdin.readline

def main() -> None:
    def check(s: str):
        d = inst[s](cur if s in ('D', 'S') else str(cur).zfill(4))
        if M[d] is None:
            q.append(d)
            M[d] = M[cur]+s
        if d == B:
            print(M[d])
            return True
        return False
    
    T = int(input())

    inst = {'D': lambda n: 2*n % 10000,
            'S': lambda n: (n-1) % 10000,
            'L': lambda s: int(s[1:]+s[0]),
            'R': lambda s: int(s[-1]+s[:-1])}
    for _ in range(T):
        A, B = map(int, input().split())
        M = [None] * 10000
        q = deque()
        
        cur = None
        q.append(A)
        M[A] = ''
        while True:
            if cur == 1987:
                print()
            cur = q.popleft()
            
            if check('D') or check('S') or check('L') or check('R'):
                break

    
if __name__ == "__main__":
    sys.exit(main())