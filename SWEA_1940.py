def f(a):
    b = 0
    c = 0
    
    for d in a:
        if d[0] == 1:
            b += d[1]
        elif d[0] == 2:
            b = max(0, b - d[1])
        
        c += b
    
    return c


e = int(input())
for i in range(1, e + 1):
    g = int(input())
    h = []
    for _ in range(g):
        h.append(list(map(int, input().split())))
    
    print(f"#{i} {f(h)}")