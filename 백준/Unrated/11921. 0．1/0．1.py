import sys
import os

input = sys.stdin.readline
print = sys.stdout.write

def main():
    n = 0
    total = 0
    a, _, b = os.read(0, 10000).decode('utf-8').rpartition('\n')
    list_a = a.split('\n')
    i = len(list_a) - 1
    m = map(int, list_a)
    m.__next__()
    total += sum(m)

    while i < 410000:
        if a == '':
            break
        temp = b
        a, _, b = os.read(0, 10000).decode('utf-8').rpartition('\n')
        a = temp + a
        list_a = a.split('\n')
        i += len(list_a)
        m = map(int, list_a)
        total += sum(m)

    print(str(i) + '\n')
    print(str(total))

main()