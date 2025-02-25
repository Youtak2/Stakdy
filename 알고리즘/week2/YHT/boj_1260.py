from collections import deque

def dfs(b):
    re.append(b)
    visit[b] = 1
    for i in a[b]:
        if visit[i] != 1:
            dfs(i)

def bfs(b):
    qu = deque([b])
    visit[b] = 1
    while qu:
        c = qu.popleft()
        re2.append(c)
        for i in a[c]:
            if visit[i] != 1: 
                qu.append(i)
                visit[i] = 1

n, m, v = map(int, input().split())
a = [[] for _ in range(n+1)]
re = []
re2 = []
visit = [0] * (n+1)

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(1, n+1):
    a[i].sort()  

dfs(v)
print(*re)

visit = [0] * (n+1) 
bfs(v)
print(*re2)
