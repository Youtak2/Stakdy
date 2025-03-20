
# for x in range(1, 5):
#     if co.count(x) == 2:
#         q.append(x)

# if q[0] == 1 and q[1] == 3:
#     ina = 1
# elif q[0] == 1 and q[1] == 4:
#     ina = 2
# elif q[0] == 2 and q[1] == 4:
#     ina = 3
# elif q[0] == 2 and q[1] == 3:
#     ina = 4

# if ina == 1 and co.index(3) > co.index(1):
#     idx = co.index(1)
#     co.append(1)
#     co2.append(co2[idx])
#     co.pop(idx)
#     co2.pop(idx)

# elif ina == 2 and co.index(1) > co.index(4):
#     idx = co.index(4)
#     co.append(4)
#     co2.append(co2[idx])
#     co.pop(idx)
#     co2.pop(idx)

# elif ina == 3 and co.index(2) < co.index(4):
#     idx = co.index(2)
#     co.append(2)
#     co2.append(co2[idx])
#     co.pop(idx)
#     co2.pop(idx)

# elif ina == 4 and co.index(3) < co.index(2):
#     idx = co.index(3)
#     co.append(3)
#     co2.append(co2[idx])
#     co.pop(idx)
#     co2.pop(idx)

# for x in range(len(co)):
#     if ina == 1 and co[x] == 3:
#         cmt = co2[x] * co2[x + 1]
#         cmt2 += cmt
#     if ina == 2 and co[x] == 1:
#         cmt = co2[x] * co2[x + 1]
#         cmt2 += cmt
#     if ina == 3 and co[x] == 4:
#         cmt = co2[x] * co2[x + 1]
#         cmt2 += cmt
#     if ina == 4 and co[x] == 2:
#         cmt = co2[x] * co2[x + 1]
#         cmt2 += cmt

# print(cmt2)
# 설계 미스아님????
# 잘못 큰거에서 작은 사각형을 해보자
a = int(input())  
co = []  
co2 = []  
w = []  
n_w = 0  
n_h = 0  
w_max = h_max = 0  

for i in range(6):
    b, c = map(int, input().split())
    co.append(b)
    co2.append(c)

for x in range(1, 5):
    if co.count(x) == 1:
        w.append(co.index(x))

z = co2[w[0]] * co2[w[1]]

for i in range(6):
    if co[i] == 1 or co[i] == 2:  
        if w_max < co2[i]:
            w_max = co2[i]
    elif co[i] == 3 or co[i] == 4:  
        if h_max < co2[i]:
            h_max = co2[i]

for i in range(6):
    if co[i] == 1 or co[i] == 2:
        if co2[(i+1) % 6] + co2[(i-1) % 6] == h_max:
            n_w = co2[i]
    elif co[i] == 3 or co[i] == 4:
        if co2[(i+1) % 6] + co2[(i-1) % 6] == w_max:
            n_h = co2[i]

area = z - (n_w * n_h)
print(area * a)


