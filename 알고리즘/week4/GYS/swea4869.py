T = int(input())
for tc in range(1, T+1):
    N = int(input())

    stack = [0] * (N+1)
    stack[10] = 1
    stack[20] = 3

    for i in range(30, N+1, 10):
        stack[i] = stack[i-10] + 2*stack[i-20]

    print(f'#{tc} {stack[N]}')