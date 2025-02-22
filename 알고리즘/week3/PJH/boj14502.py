import copy
N, M = map(int,input().split())
virus = [list(map(int,input().split())) for _ in range(N)]
list_a = []
list_s = []
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if virus[i][j] == 0:
          list_a.append((i,j))
        elif virus[i][j] == 1:
           visited[i][j] = 1
        else:
           visited[i][j] = 1
           list_s.append((i,j))

answer = []
list_b = 0
#벽을 넣을 위치 조합 구하기기
for i in range(0,len(list_a)):
   for j in range(i+1,len(list_a)):
      for k in range(j+1,len(list_a)):
         answer.append([list_a[i],list_a[j],list_a[k]])
#dfs
def dfs(arr,si,sj):
   arr[si][sj] = 1

   for d in [[1,0],[0,1],[-1,0],[0,-1]]:
      ni = si + d[0]
      nj = sj + d[1]
      if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
         dfs(arr,ni,nj)

# 벽세워주기
list_c = []
for ans in answer:
    cnt = 0
    temp = copy.deepcopy(visited)
    for a in range(3):
        i,j = ans[a]
        temp[i][j] = 1
    for s in list_s:
        si,sj = s
        dfs(temp,si,sj)
    for t in temp:
        cnt += t.count(0)
        list_c.append(cnt)
print(max(list_c))

