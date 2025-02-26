# 23:25~

sugar = int(input())

N = sugar//5
M = sugar//3
result =[]

for i in range(N+1):
    for j in range(M+1):
        if i*5 + j*3 == sugar:
            result.append(i+j)

if result == []:
    ans = -1
else:
    ans = min(result)
print(ans)


'''
num5 = 0
num3 = 0

sugar = int(input())

num5 = int(sugar//5)
sugar2 = sugar%5
num3 = int(sugar2//3)

if sugar2%3 != 0:
    if sugar%3 == 0:
        result = sugar//3
    else:

        result = -1
else:
    result = num5 + num3

print(result)
'''