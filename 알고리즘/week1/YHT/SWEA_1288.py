def a(b, c):
    d = []
    for e in range(1, b + 1):
        f = c[e - 1]
        g = set()
        h = 0
        
        while len(g) < 10:
            h += 1
            i = f * h
            g.update(str(i))
        
        d.append(f"#{e} {i}")
    
    return d

# 입력 예시
b = int(input())
c = [int(input()) for _ in range(b)]

# 결과 출력
for j in a(b, c):
    print(j)
