import time
import sys
import os

input = sys.stdin.readline
print = sys.stdout.write

def main():
    s = time.perf_counter()
    n = 0
    total = 0
    a, _, b = os.read(0, 10000).decode('utf-8').rpartition('\n')
    list_a = a.split()
    i = len(list_a) - 1
    m = map(int, list_a)
    m.__next__()
    total += sum(m)

    while time.perf_counter() < s + 0.09:
        temp = b
        a, _, b = os.read(0, 10000).decode('utf-8').rpartition('\n')
        a = temp + a
        list_a = a.split()
        i += len(list_a)
        m = map(int, list_a)
        total += sum(m)

    print(str(i) + '\n')
    print(str(total))

main()