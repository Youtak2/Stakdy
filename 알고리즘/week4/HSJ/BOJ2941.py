word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for alphabet in croatia:
  if alphabet in word:
    while alphabet in word:
      word = word.replace(alphabet, ',', 1)
      cnt += 1
word = word.replace(',', "")
cnt += len(word)

print(cnt)