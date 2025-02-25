N = int(input())
grades = list(map(int, input().split()))
new_grades = []
M = 0
sum = 0
for i in range(N):
  if grades[i] >= M:
    M = grades[i]
for i in range(N):
  new_grades.append(grades[i] / M * 100)
for i in range(N):
  sum += new_grades[i]
result = sum / N
print(result)