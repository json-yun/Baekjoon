import time
import sys
import os

input = sys.stdin.readline
print = sys.stdout.write

s = time.time()
n = 0
total = 0
fd = 0
a, _, b = os.read(fd, 20000).decode('utf-8').rpartition('\n')
m = map(int, a.split())
N = int(m.__next__())
for i, n in enumerate(m):
    if time.time() > s + 0.1:
        break
    total += n
else:
    i += 1

print(str(i) + '\n')
print(str(total))