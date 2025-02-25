# N,M,V = map(int,input().split())
# adj_dfs = [[0]*N for _ in range(N)]
# adj_bfs = [[0]*N for _ in range(N)]
# for _ in range(M):
#     r,c = map(int,input().split())
#     adj_dfs[r-1][c-1] = 1
#     adj_dfs[c-1][r-1] = 1
#     adj_bfs[r-1][c-1] = 1
#     adj_bfs[c-1][r-1] = 1


# def DFS(arr):
#     i_dfs = V-1
#     list_a = []
#     cnt = 0
#     list_a.append(V)
#     while cnt<N-1:
#         for a in arr:
#             a[i_dfs] = 0
#         i_dfs = arr[i_dfs].index(1)           
#         list_a.append(i_dfs+1)
#         cnt += 1
#     return list_a





# def BFS(arr):
#     i_bfs = V-1
#     j_bfs = V-1
#     visited = [0]*N
#     list_b = []
#     while sum(visited)!=N:
#         if sum(arr[i_bfs]) != 0:
#             visited[j_bfs] = 1
#             list_b.append(j_bfs+1)
#             j_bfs = arr[i_bfs].index(1)
#             arr[i_bfs][j_bfs] = 0
#         else:
#             i_bfs += 1
#     return list_b

# print(*DFS(adj_dfs),end=" ")
# print()
# print(*BFS(adj_bfs),end=" ")

def dfs(c):
    ans_dfs.append(c)       #방문 노드 추가
    v[c] = 1                #방문 표시

    for n in adj[c]:
        if not v[n]:  #방문하지 않은 경우우  
            dfs(n)

def bfs(s):
    q = []
    q.append(s)      #필요한 q,v[],변수 생성
    ans_bfs.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        for n in adj[c]:
            if not v[n]: #방문하지 않은 노드 큐 삽입
                q.append(n)
                ans_bfs.append(n)
                v[n] = 1

N,M,V = map(int,input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s) #양방향

for i in range(1,N+1):
    adj[i].sort()

v = [0]*(N+1)
ans_dfs = []
dfs(V)

v = [0]*(N+1)
ans_bfs = []
bfs(V)


print(*ans_dfs)
print(*ans_bfs)
