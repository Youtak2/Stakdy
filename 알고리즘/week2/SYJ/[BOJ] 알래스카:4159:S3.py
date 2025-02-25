while True:
    N = int(input())  # 고속도로에 있는 충전소의 수
    if N == 0:  # 0을 입력받으면 종료
        exit()
    result = 'POSSIBLE'  # default = 'possible'

    charge = [0] * N  # charge: 충전소 위치
    for i in range(N):
        charge[i] = int(input())  # N개의 충전소 위치 입력받기

    charge.sort()  # 충전소 위치 오름차순 정렬
    for i in range(N-1):
        if charge[i+1]-charge[i] > 200:  # 간격이 200 이상 차이날 때
            result = 'IMPOSSIBLE'
    if (1422-charge[-1])>100:  # 마지막 충전소에서 충전 후 델타정선 찍턴 후 돌아오는 거리
        result = 'IMPOSSIBLE'

    print(result)