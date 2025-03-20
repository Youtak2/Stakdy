def check(test):
    stack = []
    dic = {'(':')', '{':"}"}

    for i in test:
        if i in dic:
            stack.append(i)
        elif i in dic.values():
            if not stack:
                return '0'
            pop_stack = stack.pop()
            if dic[pop_stack] != i:
                return '0' 
            
    return '1' if not stack else '0'

T = int(input())


for tc in range(1, T+1):
    test = list(input())
    result = check(test)
    print(f'#{tc} {result}')

            
