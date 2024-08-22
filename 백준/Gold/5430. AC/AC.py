import sys
input = sys.stdin.readline

def main() -> None:
    TC = int(input())
    for _ in range(TC):
        INST = input().rstrip()
        N = int(input())
        ARR = input().rstrip().strip('[]').split(',')

        if (N := N-INST.count('D')) < 0:
            print("error")
            continue

        d = 0
        inv = False
        for inst in INST:
            if inst == 'D':
                if not inv:
                    d += 1
            else:
                inv = not inv

        ARR = ARR[d:d+N]
        if inv:
            ARR = reversed(ARR)
        print('[' + ','.join(ARR) + ']')
        
main()