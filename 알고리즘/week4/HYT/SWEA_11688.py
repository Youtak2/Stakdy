"""
L 과 R 이거 그냥 공식대로 내려가면 되네
"""
T=int(input())
for i in range(1,T+1):
    a,b=1,1
    c=list(map(str,input().strip()))
    for x in range(len(c)):
        if(c[x]=='L'):
            b=(a+b)
        elif(c[x]=='R'):
            a=(a+b)
    print(f'#{i} ',end="")
    print(a,b)