from collections import deque

def bfs(si,sj,b): #si,sj: 시작 좌표 b: 벽 부수기 유무
    q = deque()
    q.append((si,sj,b))
    visited[0][si][sj] = 1
    while q:
        r,c,brek = q.popleft()
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]
            if nr<0 or nr>=N or nc<0 or nc>=M:
                continue
            if brek == 0:
                if graph[nr][nc] == 1 and visited[1][nr][nc]==0:
                    q.append((nr,nc,brek+1))
                    visited[1][nr][nc] = visited[0][r][c] + 1
                elif graph[nr][nc] == 0 and visited[0][nr][nc] == 0:
                    q.append((nr,nc,brek))
                    visited[0][nr][nc] = visited[0][r][c] + 1
            elif brek == 1:
                if graph[nr][nc] == 0 and visited[1][nr][nc]==0:
                    q.append((nr,nc,brek))
                    visited[1][nr][nc] = visited[1][r][c] + 1


dr = [-1,1,0,0]
dc = [0,0,-1,1]

N,M = map(int, input().split())
graph = [list(map(int,input())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for _ in range(2)]
bfs(0,0,0)
if visited[0][N-1][M-1] == 0 and visited[1][N-1][M-1] == 0:
    print(-1)
else:
    if visited[0][N-1][M-1] == 0:
        print(visited[1][N-1][M-1])
    elif visited[1][N-1][M-1]==0:
        print(visited[0][N-1][M-1])
    else:
        print(min(visited[1][N-1][M-1],visited[0][N-1][M-1]))