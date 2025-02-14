T = int(input())
N,M = map(int,input().split())
russia = [list(map(input())) for _ in range(N)]
ans = 0 #색깔을 바꿔준 횟수

for i in range(N):
    for j in range(M):
        if i == 0:
            if russia[i][j] != 'W':
                russia[i][j] = 'W'
                ans += 1
        elif i == N-1:
            if russia[i][j] != 'R':
                russia[i][j] = 'R'
                ans += 1
        elif i != 1 and i != N-1:
            cnt_w = 0
            cnt_b = 0
            cnt_r = 0
            if russia[i-1][0] == 'W':
                if russia[i][j] =='W':
                    cnt_w += 1
                elif russia[i][j] == 'B':
                    cnt_b += 1
                if cnt_w>cnt_b:
                    if russia[i][j] != 'W':
                        russia[i][j] = 'W'
                        ans += 1
                else:
                    if russia[i][j] != 'B':
                        russia[i][j] = 'B'
                        ans += 1
            elif russia[N-3][0] == 'W':
                if russia[N-2][j] != 'B':
                    russia[N-2][j] = 'B'
                    ans += 1

            elif russia[i-1][0] == 'B':
                if russia[i][j] =='B':
                    cnt_b += 1
                elif russia[i][j] == 'R':
                    cnt_r += 1
                if cnt_b>cnt_r:
                    if russia[i][j]!='B':
                        russia[i][j] = 'B'
                        ans += 1
                else:
                    if russia[i][j] !='R':
                        russia[i][j] = 'R'
                        ans += 1
            else:
                if russia[i][j] != 'R':
                    russia[i][j] = 'R'
                    ans += 1

    print(ans)

