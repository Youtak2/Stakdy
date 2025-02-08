def find(l):
    for x in range(100):
        if l[99][x] == 2:
            start_x = x
            break
    
    dx = [-1, 1, 0]
    dy = [0, 0, -1]
    
    y, x = 99, start_x
    
    while y > 0:
        for d in range(2):  
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 100 and l[ny][nx] == 1:
                while 0 <= nx < 100 and l[ny][nx] == 1:
                    x = nx
                    nx += dx[d]
                break  
        y -= 1  
    
    return x

for _ in range(10):
    test_case = int(input())
    l = [list(map(int, input().split())) for _ in range(100)]
    result = find(l)
    print(f"#{test_case} {result}")