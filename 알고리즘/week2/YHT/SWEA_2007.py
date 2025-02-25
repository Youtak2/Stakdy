t=int(input())
for i in range(1,t+1):
    k=1
    a=input()
    re=[]
    while k<11:
        if(a[0:k]==a[k:2*k]):
            b=len(a[0:k])
            break
        k=k+1
    print(f"#{i} {b}")
    ##dwqdwqessdsdd33213