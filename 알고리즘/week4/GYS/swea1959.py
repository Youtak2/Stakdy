T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))
    end = max(N, M) - min(N, M)
    small = min(N, M)
    max_v = 0

    # for i in range(end+1):
    #     value = 0
    #     for j in range(small):
    #         if len(Ai) < len(Bj):
    #             plus = Ai[j] * Bj[i+j]
    #             value += plus
    #             if value > max_v:
    #                 max_v = value
    #         else :
    #             plus = Ai[i+j] * Bj[j]
    #             value += plus
    #             if value > max_v:
    #                 max_v = value

    if len(Ai) > len(Bj):
        Ai, Bj = Bj, Ai

    for i in range(end+1):
        value = sum(Ai[j] * Bj[i+j] for j in range(small))
        max_v = max(max_v, value)

    print(f'#{tc} {max_v}')