def bfs(N,K):
    q = []
    visited = [0]*2000001
    visited[N] = 1
    q.append(N)
    while q:
        ci = q.pop(0)
        dir = [-1,1,ci]
        if ci == K:
            return visited[K]-1
        for di in dir:
            ni = ci+di
            if 0<=ni<=200000 and visited[ni] == 0:
                q.append(ni)
                visited[ni] = visited[ci] + 1
            



N, K = map(int,input().split())
print(bfs(N,K))


