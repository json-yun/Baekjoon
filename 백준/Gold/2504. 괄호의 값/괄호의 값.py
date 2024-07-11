# 스택은 자연스럽게 정렬된 상태가 된다.
import sys

A :list[str] = list(sys.stdin.readline()[:-1])

class Stack:
    def __init__(self) -> None:
        self.data = []
        self.last = None
    def push(self, data :str) -> None:
        self.data.append(data)
        self.last = data
    def pop(self) -> str:
        if self.data:
            if len(self.data)>1:
                self.last = self.data[-2]
            else:
                self.last = None
            return self.data.pop(-1)
        else:
            return None

def main() -> int | None:
    # 한 항의 값을 반환하는 함수(단일 괄호인 경우 값을 출력한다.)
    def _term(s :str):
        stack = Stack()
        if s in bracket:
            stack.push(s)
        else:
            return None
        
        term_value = 0
        # 스택이 비지 않은 경우(같은 항인 경우)
        while stack.last is not None:
            # 다음 글자를 가져온다.
            if len(A) <= 0:
                return None
            next = A.pop(0)
            # 다음 글자가 열리는 괄호면 덧셈
            if next in bracket:
                if (term := _term(next)) is None:
                    return None
                else:
                    term_value += term
            # 다음 글자가 닫히는 괄호면 곱셈
            else:
                pop = stack.pop()
                #알맞게 닫힌 경우에만
                if next == bracket[pop]:
                    if term_value == 0:
                        term_value = 1
                    term_value *= bracket_value[pop]
                else:
                    return None
        # 이번 항은 끝남
        return term_value
        
    bracket = {'(': ')',
               '[': ']'}
    bracket_value = {'(': 2,
                     '[': 3}
    result = 0
    while A:
        if (term := _term(A.pop(0))) is None:
            result = 0
            break
        else:
            result += term
    print(result)

main()