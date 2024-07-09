import sys

N = int(sys.stdin.readline())

class Queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = 0
    def push(self, n :int) -> None:
        self.data.append(n)
        self.tail += 1
    def pop(self) -> int:
        if self.head != self.tail:
            self.head += 1
            return self.data[self.head-1]
        else:
            return -1
    def size(self) -> int:
        return self.tail-self.head
    def empty(self) -> int:
        return 0 if self.size() else 1
    def front(self) -> int:
        if not self.empty():
            return self.data[self.head]
        else:
            return -1
    def back(self) -> int:
        if not self.empty():
            return self.data[self.tail-1]
        else:
            return -1
        
def main() -> None:
    queue = Queue()
    lines = [[i for i in sys.stdin.readline().split()] for _ in range(N)]
    for line in lines:
        if line[0] == "push":
            queue.push(int(line[1]))
        elif line[0] == "pop":
            print(queue.pop())
        elif line[0] == "size":
            print(queue.size())
        elif line[0] == "empty":
            print(queue.empty())
        elif line[0] == "front":
            print(queue.front())
        elif line[0] == "back":
            print(queue.back())

main()