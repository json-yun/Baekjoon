class Number:
    def __init__(self):
        self.number = [0,0,0,0,0,0,0,0,0,0]

    def increase(self):
        for i in range(10):
            if self.number[i] == 9:
                if i >= 9:
                    raise ValueError("감소하는 수 없음")
                self.number[:i+2] = list(range(i+2))
                break
            elif self.number[i+1] == 0 or self.number[i]+1 < self.number[i+1]:
                self.number[i] += 1
                self.number[:i] = list(range(i))
                break

    def print(self):
        end = self.number.index(max(self.number))
        print(''.join(map(str, reversed(self.number[:end+1]))))

N = int(input())
number = Number()

try:
    for i in range(N):
        number.increase()
    number.print()
except ValueError:
    print(-1)