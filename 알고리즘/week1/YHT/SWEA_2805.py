a = int(input())
for i in range(1, a + 1):
    t = int(input())
    result = [[0] * (j + 1) for j in range(t)]

    print(f'#{i}')

    for j in range(t):
        for k in range(j + 1):
            if j == k or k == 0:
                result[j][k] = 1
            else:
                result[j][k] = result[j-1][k] + result[j-1][k-1]

    for row in result:
        print(" ".join(map(str, row)))