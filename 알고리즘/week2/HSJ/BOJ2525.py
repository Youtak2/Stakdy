A, B = map(int, input().split())
C = int(input())

if B+C < 60:
  print(f'{A} {B+C}')
else:
  h = (B+C) // 60
  m = (B+C)-(h*60)
  if A+h < 24:
    print(f'{A+h} {m}')
  else:
    print(f'{A+h-24} {m}')