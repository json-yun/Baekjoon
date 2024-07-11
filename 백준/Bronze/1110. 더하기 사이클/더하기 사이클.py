import sys

def generate(n: int) -> int:
    global count
    count += 1
    new = sum(int(i) for i in list(str(n)))%10
    return n%10*10+new

start = int(sys.stdin.readline().strip())

n = start
count = 0
n = generate(n)
while n != start:
    n = generate(n)
print(count)