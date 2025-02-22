n = int(input())


list_cnt = []
for x in range(1,n+1):
    list_n = [n,x]
    cnt=0
    while True:
        if ((list_n[-2]-list_n[-1])>=0) and (x<=n):
            list_n.append(list_n[-2]-list_n[-1])
            cnt += 1
        else:
            list_cnt.append(cnt)
            break
print(max(list_cnt)+2)
list_n = [n,list_cnt.index(max(list_cnt))+1]
while True:
    if ((list_n[-2]-list_n[-1])>=0) and (x<=n):
        list_n.append(list_n[-2]-list_n[-1])
    else:
        break
for lst in list_n:
    print(lst,end=" ")

            