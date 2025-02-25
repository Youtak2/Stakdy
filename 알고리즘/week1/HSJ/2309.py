dwarf = []
for _ in range(9):
  dwarf.append(int(input()))

answer = []
def comb(cnt, idx):
  if cnt == 7:
    if sum(answer) == 100:
      for j in sorted(answer):
          print(j)
      exit()
    else:
      return
  for i in range(idx, 9):
    answer.append(dwarf[i])
    comb(cnt+1, i+1)
    answer.pop()
comb(0, 0)