n = int(input())
numbers = list(map(int, input().split()))  
line = []

for i in range(n):
    line.insert(len(line) - numbers[i], i + 1)

print(" ".join(map(str, line)))
##  ####
