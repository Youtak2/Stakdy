# T = int(input())
# paper = [list(map(int, input().split())) for _ in range(T)]

# # 전체 합 구하기
# # 겹친 부분 빼기

# all = 100*T
# double = 0

# for i in range(T):
#     for j in range(i+1, T):
#         x1, y1 = paper[i]
#         x2, y2 = paper[j]
        
#         height = 10 - abs(y1 - y2)
#         width = 10 - abs(x1 - x2)

#         if width > 0 and height > 0:
#             double += height * width
                

# result = all - double

# print(result)

T = int(input())

paper_map = [[0]*100 for _ in range(100)]
result = 0

for tc in range(T):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            paper_map[i][j] = 1

for k in range(100):
    for l in range(100):
        if paper_map[k][l] == 1:
            result += 1

print(result)