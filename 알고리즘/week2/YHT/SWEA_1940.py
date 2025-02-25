T=int(input())
for i in range(1,T+1):
    a=int(input())
    b=[list(map(int,input().split())) for _ in range(a)]
    if b[0][0]==0:
        current=0
    else:
        current=b[0][1]/b[0][0]
    cnt=current
    for j in range(1,a):
        if(b[j][0]==1):
            current+=b[j][1]
            cnt+=current
        elif(b[j][0]==2):
            current-=b[j][1]
            if(current<0):
                current=0
            cnt+=current
        else:
            cnt+=current
            
    print(f'#{i} {int(cnt)}')