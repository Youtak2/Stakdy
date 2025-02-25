T=int(input())
for i in range(1,T+1):
    a=int(input())
    b=list(map(int,input().split()))
    re=[]
    for j in range(a):
        re.append(abs(b[j]))
    c=min(re)
    d=re.count(c)
    print(f'#{i} {c} {d}')