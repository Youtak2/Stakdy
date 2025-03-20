def dfs(r, c, dir):
    global cnt
    # 현재 위치 청소
    if robot[r][c] == 0:
        robot[r][c] = 2
        cnt += 1  # 청소한 칸 개수 증가

    # 4방향 탐색
    for i in range(4):
        ndir = (dir + 3) % 4  # 반시계 방향 회전
        nr = r + dr[ndir]
        nc = c + dc[ndir]

        if 0 <= nr < N and 0 <= nc < M and robot[nr][nc] == 0:  # 청소할 수 있는 경우
            dfs(nr, nc, ndir)
            return  # 재귀 호출 후 되돌아오면 중복 탐색 방지

        dir = ndir  # 방향 업데이트 (왼쪽으로 계속 돈다)

    # 네 방향 모두 청소할 수 없는 경우 → 후진 가능 여부 확인
    back_dir = (dir + 2) % 4  # 후진 방향 (현재 방향의 반대)
    br, bc = r + dr[back_dir], c + dc[back_dir]

    if 0 <= br < N and 0 <= bc < M and robot[br][bc] != 1:  # 벽이 아니면 후진
        dfs(br, bc, dir)


# 입력
N, M = map(int, input().split())
r, c, d = map(int, input().split())

# 맵에서 0: 청소되지 않음, 1: 벽
robot = [list(map(int, input().split())) for _ in range(N)]

# 방향 정의 (0:북, 1:동, 2:남, 3:서)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0  # 청소한 칸 수
dfs(r, c, d)

print(cnt)