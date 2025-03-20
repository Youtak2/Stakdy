T=1
for i in range(1,T+1):
    a=int(input())
    b=[list(map(int,input().split())) for _ in range(a)]
    for x in range(a):
        if(b[x]==1 or b[x]==2):
            
