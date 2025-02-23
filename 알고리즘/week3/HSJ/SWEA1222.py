for tc in range(1, 11):
  length = int(input())
  expression = input()

  output = []
  stack = []
  result = 0


  for i in expression:
    if i.isdecimal():
      output.append(i)
    else:
      stack.append(i)
    while stack:
      output.append(stack.pop())

  for i in output:
    if i != "+":
      result += int(i)

  print(f'#{tc} {result}')