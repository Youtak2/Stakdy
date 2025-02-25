student = []
for i in range(28):
  number = int(input())
  student.append(number)

noapply = []
for j in range(1, 31):
  if j not in student:
    noapply.append(j)

noapply.sort()
print(noapply[0])
print(noapply[1])