"""
팰린드롬 구하기 회문 이걸 어캐 할까...?11*11 121 N/a=a 이인 것들을 뽑고 그다음에 이걸 리스트에 넣고 ::-1 을 했을때
원본과 비교해서 같으면 cnt 증가
a,b포함
"""

def change(a,n):
    k=[]
    for x in range(n):
        if(100<=a[x]<=1000):
            b=a[x]//100
            v=a[x]%100
            c=v//10
            d=v%10
            e=d*100+c*10+b
            k.append(e)
        elif(10<=a[x]<100):
            c=a[x]//10
            d=a[x]%10
            e=d*10+c
            k.append(e)
        else:
            e=a[x]
            k.append(e)
    return k
        


T=int(input())
for i in range(1,T+1):
    a,b=map(int,input().split())
    c=[]
    cnt=0
    v=[]
    for x in range(a,b+1):
        for y in range(1,b+1):   
            if(y**2==x):
                c.append(x)
                v.append(y)
    print(f'#{i} ',end='')
 
    w=[]
    w=change(c,len(c))
    z=[]
    z=change(v,len(v))
    for x in range(len(c)):
        if(c[x]==w[x] and z[x]==v[x]):
            cnt+=1
    print(cnt)
    # for x in range(len(c)):
    #     if(c[x]<10):
    #         cnt+=1
    #     else:
    #         c=list(c)


    
