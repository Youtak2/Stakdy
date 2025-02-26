n=int(input())
a=list(map(int,input().split()))
c,d=map(int,input().split())
a.sort()
e=(a[-1]//c)+1
sum=0
for i in range(0,len(a)):
    if(a[i]%c==0):
        sum+=a[i]/c
    else:
        sum+=(a[i]//c)+1
g=n//d
f=n%d
print(int(sum))
print(g,f)

