# 스택은 자연스럽게 정렬된 상태가 된다.
import random
import sys

N = int(sys.stdin.readline())
A = [int(i) for i in sys.stdin.readline().split()]

class Stack:
    def __init__(self) -> None:
        self.data = []
        self.index = []
        self.last = None
    def push(self, data :int, index :int) -> None:
        self.data.append(data)
        self.index.append(index)
        self.last = data
    def pop(self) -> tuple[int | None]:
        if self.data and self.index:
            if len(self.data)>1:
                self.last = self.data[-2]
            else:
                self.last = None
            return self.data.pop(-1), self.index.pop(-1)
        else:
            return None, None

def main() -> None:
    stack = Stack()

    answer = ['0' for _ in range(N)]
    stack.push(A[N-1], N-1)
    for i in range(N-2, -1, -1):
        while (stack.last is not None) and stack.last <= A[i]:
            _, idx = stack.pop()
            answer[idx] = str(i+1)
        stack.push(A[i], i)

    print(" ".join(answer))

main()