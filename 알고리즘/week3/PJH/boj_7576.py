from collections import deque
dr = [1,0,-1,0]
dc = [0,1,0,-1]

def bfs(arr):
    q = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i,j))
                visited[i][j] = 1
            elif arr[i][j] == -1:
                visited[i][j] = -1

    while q:
        si,sj = q.popleft()
        for i in range(4):
            ni = si + dr[i]
            nj = sj + dc[i]
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] != 0 or visited[ni][nj] != 0:
                    continue
                visited[ni][nj] = visited[si][sj] + 1
                q.append((ni,nj))


M,N = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
max_v = 0
bfs(tomato)
cnt = 0
for v in visited:
    cnt += v.count(0)

if cnt == 0:
    for v in visited:
        max_v = max(max_v,max(v))
    print(max_v-1)
else:
    print(-1)