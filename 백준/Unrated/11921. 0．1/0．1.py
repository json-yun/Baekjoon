import time

N = int(input())
s = time.time()
n = 0
total = 0
while time.time() < s + 0.09 and n < N:
    n += 1
    total += int(input())

print(n)
print(total)