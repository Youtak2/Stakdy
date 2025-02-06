list_rect = [list(map(int,input().split())) for _ in range(4)]

list_a = [[0]*100 for _ in range(100)]


for i in range(4):
    for a in range(100-list_rect[i][3],100-list_rect[i][1]):
        for b in range(list_rect[i][0],list_rect[i][2]):
            if list_a[a][b]==0:
                list_a[a][b] += 1
cnt = 0
for i in range(100):
    cnt += sum(list_a[i])

print(cnt)

