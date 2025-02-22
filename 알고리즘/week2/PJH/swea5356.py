T = int(input())
for tc in range(1,T+1):
    list_str = [list(input()) for _ in range(5)]
    len_str = []
    left_a = []
    right = []
    for i in range(5):
        len_str.append(len(list_str[i]))
    j = min(len_str)
    while j <= max(len_str):
        for i in range(5):   
            if len_str[i] > j:
                left_a += list_str[i][j]
        j += 1
    for c in range(min(len_str)):
        for st in list_str:
            right += st[c]
    ans = ''.join(right) + ''.join(left_a)
    print(f'#{tc} {ans}')            