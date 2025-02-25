from collections import deque

def DFS(v, seq):
  visited[v] = 1

  for i in range(1, N+1):
    if visited[i] != 1 and arr[v][i] == 1:
      seq = DFS(i,seq+[i])
  
  return seq


def BFS(v, seq):
  q = deque()
  q.append(v)
  visited[v] = 1

  while q:
    n = q.popleft()
    seq.append(n)
    for i in range(1, N+1):
      if visited[i] != 1 and arr[n][i] == 1:
        visited[i] = 1
        q.append(i)

  return seq


N, M, V = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  arr[a][b] = arr[b][a] = 1

visited = [0] * (N+1)
d_result = DFS(V, [V])
visited = [0] * (N+1)
b_result = BFS(V, [])

print(*d_result)
print(*b_result)