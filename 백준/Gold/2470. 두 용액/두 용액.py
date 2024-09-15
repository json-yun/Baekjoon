import sys
input = sys.stdin.readline

def main() -> None:
    def find_nearest(n: int, frm: list) -> tuple:
        # 이분 탐색으로 변경
        btm, top = 0, len(frm)-1
        while btm < top-1:
            mid = (btm+top)//2
            if frm[mid] > n:
                top = mid
            elif frm[mid] == n:
                btm = mid
                top = mid
            else:
                btm = mid

        return frm[btm], frm[top]
    
    N = int(input())
    PH = input().split()
    acids = []
    bases = []
    for i in PH:
        a = int(i)
        if a >= 0:
            bases.append(a)
        else:
            acids.append(a)
    acids.sort()
    bases.sort()

    neutr = 2000000000
    if len(bases) >= 2:
        mixture = abs(bases[0] + bases[1])
        if mixture < neutr:
            neutr = mixture
            answer = (bases[0], bases[1])
            
    if len(acids) >= 2:
        mixture = abs(acids[-2] + acids[-1])
        if mixture < neutr:
            neutr = mixture
            answer = (acids[-2], acids[-1])

    if (bases and acids):
        for acid in acids:
            if neutr == 0:
                break
            for base in find_nearest(abs(acid), bases):
                mixture = abs(acid+base)
                if mixture < neutr:
                    neutr = mixture
                    answer = (acid, base)
            
    print(*answer)

if __name__ == "__main__":
    sys.exit(main())