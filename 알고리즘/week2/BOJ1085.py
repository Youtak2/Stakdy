x, y, w, h = map(int, input().split())

search = [x, w-x, y, h-y]
min = x
for i in range(1, 4):
  if search[i] < min:
    min = search[i]

print(min)