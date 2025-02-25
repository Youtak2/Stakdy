while True:
    N = int(input())
    if N == 0:
        break

    loc = [int(input()) for _ in range(N)]
    loc.append(0)  # 시작점 추가
    loc.sort()

    possible = True
    for i in range(len(loc) - 1):
        if loc[i + 1] - loc[i] > 200:  # 주유소 간 거리 체크
            possible = False
            break

    # 마지막 주유소에서 1422km까지의 거리가 100km 이하인지 확인
    if (1422 - loc[-1]) > 100:
        possible = False

    print("POSSIBLE" if possible else "IMPOSSIBLE")
