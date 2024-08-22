def main() -> None:
    TC = int(input())

    for _ in range(TC):
        INST = input().rstrip()
        N = int(input())
        ARR = [i for i in input().strip('[]').split(',')]

        d_count = 0
        inv = False
        for inst in INST:
            if inst == 'D':
                N -= 1
                if N < 0:
                    break
                if not inv:
                    d_count += 1
            else:
                inv = not inv

        if N >= 0:
            ARR = ARR[d_count:d_count+N]
            if inv:
                ARR = reversed(ARR)
            answer = '[' + ','.join(ARR) + ']'

            print(answer)
        else:
            print("error")
        
main()