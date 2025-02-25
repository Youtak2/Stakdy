N = int(input())
colpaper = [list(map(int,input().split())) for _ in range(N)]
list_ans = [[0]*100 for _ in range(100)]
for k in range(N):
    a,b = colpaper[k]
    for i in range(a,a+10):
        for j in range(b,b+10): 
            list_ans[j][i] = 1
    ans = 0
for i in range(100):
    for j in range(100):
        if list_ans[i][j] == 1:
            ans += 1
print(ans)
