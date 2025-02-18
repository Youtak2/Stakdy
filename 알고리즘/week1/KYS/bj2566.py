arr = []

for i in range(9):
    arr.append(list(map(int, input().split())))

arr_max = max(map(max, arr))

print(arr_max)

for i in range(9):
    for j in range(9):
        if arr[i][j] == arr_max:
            a,b = i+1, j+1
print(a,b)