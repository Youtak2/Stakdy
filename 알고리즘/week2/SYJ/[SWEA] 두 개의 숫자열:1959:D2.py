T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = []

    if N > M:
        N, M = M, N
        A, B = B, A


    for j in range(M-N+1):
        sum = 0
        for i in range(N):
            sum += A[i]*B[i+j]
        result.append(sum)

    print(f'#{tc+1} {max(result)}')