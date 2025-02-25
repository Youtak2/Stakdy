# 우, 하, 좌, 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# dfs 함수 정의
def dfs(cur_row, cur_col):
    # 예외 조건: index 범위 밖 or 0일때
    if cur_row < 0 or cur_row >= M or cur_col < 0 or cur_col >= N:
        return
    elif board[cur_row][cur_col] == 0:
        return
    
    # 배추가 심어져있는 경우(=1)
    elif board[cur_row][cur_col] == 1:
        board[cur_row][cur_col] = 0         # 방문처리 대신 해당 값을 0으로 바꿈
        for i in range(4):                  # 4방 탐색을 하면서 dfs 호출
            next_row = cur_row + dx[i]
            next_col = cur_col + dy[i]
            dfs(next_row,next_col)


T = int(input())                            # tc 입력   
for tc in range(T):
    M, N, K = map(int, input().split())     # M: 가로 길이(=num(col)), N: 세로 길이(=num(row)), K: 배추 개수
    
    board = [[0]*N for _ in range(M)]       # N*M 논: 초기값 = 0 
    for k in range(K):
        X, Y = map(int, input().split())
        board[X][Y] = 1                     # X, Y 좌표 입력 받아서 해당 위치 1로 변경 (배추 위치)

    cnt = 0                                 # 벌레 개수 count
    for i in range(M):
        for j in range(N):
            if board[i][j] == 1: 
                cnt += 1
                dfs(i, j)
                    
        
    print(cnt)
    
