numbers = []
max = 0
max_row = 0
max_coloumn = 0
for i in range(9):
  row = list(map(int, input().split()))
  numbers.append(row)
  for j in range(9):
    if max < numbers[i][j]:
      max = numbers[i][j]
      max_row = i
      max_coloumn = j

print(max)
print(f'{max_row+1} {max_coloumn+1}')