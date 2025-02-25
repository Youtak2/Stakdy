T=int(input())
for i in range(1,T+1):
    a,b=map(int,input().split())
    d=[[0]*(a+2) for _ in range(a+2)]
    c=[list(map(int,input().split())) for _ in range(a)]
    #padding 
    count=0
    #copy
    re=[list(_) for _ in zip(*d)]
    for x in range(1,a+1):
        for y in range(1,a+1):
            d[x][y]=c[x-1][y-1]
    for x in range(1,a+1):
        for y in range(1,b+1):
            if(d[x][y:y+b].count(1)==b and d[x][y-1]==0 and d[x][y+b]==0):
               count+=1    #행만했음 개미쳤다
    for x in range(1,a+1):
        for y in range(1,b+1):
            if(re[x][y:y+b].count(1)==b and re[x][y-1]==0 and re[x][y+b]==0):
               count+=1  

    print(f'#{i} {count}')