import sys

dwarfs = [int(sys.stdin.readline()) for _ in range(9)]

residual = sum(dwarfs)-100
for i, d in enumerate(dwarfs):
    if residual!=d*2 and residual-d in dwarfs:
        dwarfs.pop(i)
        dwarfs.pop(dwarfs.index(residual-d))
        break

for d in sorted(dwarfs):
    print(d)