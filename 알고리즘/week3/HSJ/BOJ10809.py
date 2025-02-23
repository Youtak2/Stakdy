from string import ascii_lowercase

S = input()
alphabet = list(ascii_lowercase)
ans_list = []
for i in range(len(alphabet)):
  answer = S.find(alphabet[i])
  ans_list.append(answer)

print(*ans_list)