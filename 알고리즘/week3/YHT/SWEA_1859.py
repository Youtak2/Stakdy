def f(a):
    b = 0
    c = 0
    
    for d in reversed(a):
        if d > b:
            b = d
        else:
            c += b - d
    
    return c

T = int(input().strip())
for t in range(1, T + 1):
    N = int(input().strip())
    a = list(map(int, input().split()))
    
    r = f(a)
    print(f"#{t} {r}")
