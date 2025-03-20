"""
bit 연산자로? 아니면 바꾸기 함수로? 바꾸기 함수로 가자

"""
def change(a,n):
    global cnt
    cnt=0
    for x in range(n):
        if(a[x]==1):
            a[x]=0
            cnt+=1
            for y in range(x+1,n):
                if(a[y]==0):
                    a[y]=1
                else:
                    a[y]=0

T=int(input())
for i in range(1,T+1):
    a=list(map(int,input().strip()))
    print(f'#{i} ',end="")
    change(a,len(a))
    print(cnt)