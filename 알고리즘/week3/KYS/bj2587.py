def bubble(num):
    for i in range(5):
        for j in range(0, 4-i):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return num

num = [int(input()) for _ in range(5)]
all_sum = 0

for i in range(5):
    all_sum += num[i]

mean = all_sum // 5

sort_num = bubble(num)
mid = sort_num[2]

print(f'{mean}\n{mid}')