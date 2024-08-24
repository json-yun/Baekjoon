def main() -> None:
    TARGET = int(input())
    LEN = len(str(TARGET))
    N = int(input()) # # of broken buttons
    if N:
        BROKEN = input().split()
    else:
        BROKEN = []
    if len(BROKEN) == 10:
        print(abs(TARGET-100))
        return
    
    for i in range(500001):
        if TARGET-i >= 0 and all(b not in str(TARGET-i) for b in BROKEN):
            print(min(i+len(str(TARGET-i)), abs(TARGET-100)))
            break
        if all(b not in str(TARGET+i) for b in BROKEN):
            print(min(i+len(str(TARGET+i)), abs(TARGET-100)))
            break

main()