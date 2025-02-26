T = int(input())

for tc in range(1, 1+T):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    cnt = []
    # 첫 줄은 무조건 흰색
    # 마지막 줄은 무조건 빨간색
    # 남은 줄(N-2개)은 W,B,R 조합 구하기
    # 단 B는 1 이상이어야 함
    for w in range(1, N-1):
        for b in range(1, N-w):
            r = N - w - b
            
            temp_cnt = 0
            
            # 중간에 색칠 카운트 하기
            for i in range(w):
                for j in range(M):
                    if flag[i][j] != 'W':
                        temp_cnt += 1

            for i in range(w, w+b):
                for j in range(M):
                    if flag[i][j] != 'B':
                        temp_cnt += 1

            for i in range(w+b, N):
                for j in range(M):
                    if flag[i][j] != 'R':
                        temp_cnt += 1

            cnt.append(temp_cnt)
    min_v = min(cnt)

    print(f'#{tc} {min_v}')