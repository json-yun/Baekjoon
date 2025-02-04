import time
import sys
import os

input = sys.stdin.readline
print = sys.stdout.write

s = time.time()
n = 0
total = 0
m = map(int,os.read(0, 3000000).decode('utf-8').split())
N = int(m.__next__())
while time.time() < s + 0.08 and n < N:
    n += 1
    total += int(m.__next__())

print(str(n) + '\n')
print(str(total))