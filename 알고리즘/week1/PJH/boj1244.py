# T = int(input())
# list_i = []
# if T%20 ==0:
#     list_a = [list(map(int,input().split())) for _ in range(T//20)]
# else:
#     list_a = [list(map(int,input().split())) for _ in range((T//20)+1)]
# for lst in list_a:
#     list_i = list_i +lst

# N = int(input())

# list_b = [list(map(int,input().split())) for _ in range(N)]
import sys

T = int(sys.stdin.readline())
list_i = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
list_b = []
for _ in range(N):
    list_b.append(list(map(int, sys.stdin.readline().split())))

for ls in list_b:
    if ls[0] == 1:
        for i in range(T):
            if (i+1)%ls[1]==0:
                list_i[i] = 1-list_i[i]
    else:
        i = ls[1]-1
        k=1
        while (i-k>=0) and (i+k<T) and (list_i[i-k]==list_i[i+k]):
             k+=1
        for _ in range(i-(k-1),i+k):
            list_i[_] = 1 -list_i[_]

for i, value in enumerate(list_i, 1):  # 1부터 인덱스 시작
    print(f"{value}", end=" ")  # 가독성을 위해 5칸 확보
    if i % 20 == 0:  # 20개 출력 후 개행
        print()




    # else:
    #     i = ls[1]-1
    #     k=1
    #     while (i-k>=0) and (i+k<T) and (list_i[i-k]==list_i[i+k]):
    #          list_i[i-k] = 1-list_i[i-k]
    #          list_i[i+k] = 1-list_i[i+k]
    #          k+=1
