a=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
T=int(input())
for i in range(1,T+1):
    b=str(input())
    print(f'#{i} ',end='')
    for x in range(0,len(a)):
        if(b==a[x]):
            v=x+1
            v=7-v
    if(v==0):
        print('7')
    else:
        print(v)
            