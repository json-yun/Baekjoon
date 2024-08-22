def main() -> None:
    TC = int(input())

    for _ in range(TC):
        INST = input()
        N = int(input())
        ARR = input().strip('[]').split(',')

        if INST.count('D') > N:
            print("error")
            continue

        d_count = 0
        inv = False
        for inst in INST:
            if inst == 'D':
                N -= 1
                if not inv:
                    d_count += 1
            else:
                inv = not inv

        ARR = ARR[d_count:d_count+N]
        if inv:
            ARR = reversed(ARR)
        print('[' + ','.join(ARR) + ']')
        
main()