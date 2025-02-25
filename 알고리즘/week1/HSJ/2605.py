students = int(input())
number = list(map(int, input().split()))

line = [1]
for i in range(1, students):
  if number[i] == 0:
    line.append(i+1)
  elif number[i] == i:
    line.insert(0, i+1)
  else:
    idx = len(line)
    line.insert(idx - number[i], i + 1)

for j in range(students):
  print(line[j], end = " ")

  '''
  예를 들어서
  5
  0 1 0 3 2

  1
  2 1
  2 1 3
  4 2 1 3
  4 2 5 1 3
  '''