import time
import sys
import os

input = sys.stdin.readline
print = sys.stdout.write

def main():
    s = time.time()
    n = 0
    total = 0
    fd = 0
    byte = 10000
    a, _, b = os.read(fd, byte).decode('utf-8').rpartition('\n')
    list_a = a.split()
    m = map(int, list_a)
    m.__next__()
    for i, n in enumerate(m, 1):
        total += n
        if time.time() > s + 0.9:
            break

    while time.time() < s + 0.07:
        temp = b
        a, _, b = os.read(fd, byte).decode('utf-8').rpartition('\n')
        a = temp + a
        list_a = a.split()
        m = map(int, list_a)
        for i, n in enumerate(m, i+1):
            total += n
            if time.time() > s + 0.9:
                break

    print(str(i) + '\n')
    print(str(total))

main()