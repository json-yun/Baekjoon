def main():
    N = int(input())

    a_n = 3
    a_n1 = 1 # n-2까지의 합
    for _ in range(N-1):
        a_n, a_n1 = (a_n + 2 + 2*a_n1)%9901, (a_n1+a_n)%9901
        
    print(a_n)

main()