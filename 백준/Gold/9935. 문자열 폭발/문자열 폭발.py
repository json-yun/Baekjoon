def main():
    STRING = list(input().rstrip())
    C4 = list(input().rstrip())

    L = len(C4)
    check_stack = []
    cnt_stack = []

    cnt = -1
    for s in STRING:
        cnt += 1
        if s != C4[cnt]:
            cnt = 0 if s == C4[0] else -1
        
        if cnt == L-1:
            for _ in range(L-1):
                check_stack.pop()
                cnt_stack.pop()
                
            cnt = cnt_stack[-1] if cnt_stack else -1
        else:
            check_stack.append(s)
            cnt_stack.append(cnt)
        
    result = ''.join(check_stack)
    print(result if result != '' else "FRULA")

main()