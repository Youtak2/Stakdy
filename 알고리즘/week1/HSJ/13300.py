N, K = (map(int, input().split()))
students = []
for i in range(N):
  s, g = (map(int, input().split()))
  students.append([s, g])

result = 0
for i in range(2):
  for j in range(1, 7):
    if [i, j] in students:
      if students.count([i, j]) <= K:
        result += 1
      elif students.count([i, j]) % K == 0:
        result += students.count([i, j]) // K
      else:
        result += students.count([i, j]) // K + 1

print(result)