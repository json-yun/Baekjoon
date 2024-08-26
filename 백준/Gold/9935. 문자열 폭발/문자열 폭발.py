def main():
    STRING = list(input().rstrip())
    C4 = list(input().rstrip())

    L = len(C4)
    check_stack = []
    cnt_stack = []

    cnt = -1
    for s in STRING:
        if s == C4[cnt+1]:
            cnt += 1
        elif s == C4[0]:
            cnt = 0
        else:
            cnt = -1
            
        if cnt == L-1:
            for _ in range(L-1):
                check_stack.pop()
                cnt_stack.pop()
            cnt = cnt_stack[-1] if cnt_stack else -1
        else:
            check_stack.append(s)
            cnt_stack.append(cnt)
        
    result = ''.join(check_stack)

    if result == '':
        print("FRULA")
    else:
        print(result)

main()