def move(y, x):
  if y == 0:
    return x

  for di, dj in [[0, -1], [0, 1], [-1, 0]]:
    ni, nj = y + di, x + dj
    if ni >= 0 and ni < 100 and nj >= 0 and nj < 100:
      if visited[ni][nj] != 1 and arr[ni][nj] == 1:
        visited[ni][nj] = 1
        break
      else:
        continue

  return move(ni, nj)

for _ in range(10):
  tc = int(input())
  arr = [list(map(int, input().split())) for _ in range(100)]
  end = arr[99].index(2)
  visited = [[0]*100 for _ in range(100)]
  visited[99][end] = 1
  
  result = move(99, end)
  
  print(f'#{tc} {result}')