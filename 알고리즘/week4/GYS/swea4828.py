T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    max_v = max(num)
    min_v = min(num)

    result = max_v - min_v

    print(f'#{tc} {result}')