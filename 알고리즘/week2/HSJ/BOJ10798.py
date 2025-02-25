words = [list(input()) for _ in range(5)]
for j in range(15):
  for i in range(5):
    if j > len(words[i]) - 1:
      continue
    else:
      print(words[i][j], end="")