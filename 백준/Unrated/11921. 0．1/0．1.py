import time
import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
s = time.time()
n = 0
total = 0
while time.time() < s + 0.099 and n < N:
    n += 1
    total += int(input())

print(str(n) + '\n')
print(str(total))