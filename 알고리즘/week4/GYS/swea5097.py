from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    rotate = deque(arr)

    for i in range(M):
        a = rotate.popleft()
        rotate.append(a)

    result = rotate[0]
    print(f'#{tc} {result}')