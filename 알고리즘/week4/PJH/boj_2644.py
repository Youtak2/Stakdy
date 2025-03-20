def bfs(s,e):
    q = []
    v = [0]*(N+1)

    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        if c == e:
            return v[e]-1

        for n in adj[c]:
            if not v[n]:
                q.append(n)
                v[n] += v[c]+1
    return -1

N = int(input())
S, E = map(int,input().split())
M = int(input())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    p, c = map(int,input().split())
    adj[p].append(c)
    adj[c].append(p)

ans = bfs(S,E)
print(ans)