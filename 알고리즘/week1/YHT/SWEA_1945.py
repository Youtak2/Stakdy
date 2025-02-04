n=int(input())
for i in range(1,n+1):
    a=int(input())
    b,c,d,e,f=0,0,0,0,0
    while(a>1):
        if(a%2==0):
            a=a/2
            b+=1
        elif(a%3==0):
            a=a/3
            c+=1
        elif(a%5==0):
            a=a/5
            d+=1
        elif(a%7==0):
            a=a/7
            e+=1
        elif(a%11==0):
            a=a/11
            f+=1
    print(f"#{i} ",end="")
    print(b,c,d,e,f,end=" ")
    print()