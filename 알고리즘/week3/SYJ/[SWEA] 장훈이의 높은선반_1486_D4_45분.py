def subset_comb(cnt,idx):
    result.append(sum(ans))
    if cnt == len(num):
        return

    for i in range(idx,len(num)):
        ans.append(num[i])
        subset_comb(cnt+1,i+1)
        ans.pop()

T = int(input())
for tc in range(T):
    N, B = map(int,input().split())
    num = list(map(int, input().split()))
    S = sum(num)
    ans = []
    result = []

    subset_comb(0,0)
    height = []
    for i in result:
        if i >= B:
            height.append(i)


    print(f'#{tc+1}', min(height)-B)