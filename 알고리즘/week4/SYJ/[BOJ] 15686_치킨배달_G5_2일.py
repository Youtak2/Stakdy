<<<<<<< Updated upstream
# 두 지점 사이 거리 함수 구현
def dist_ft(A,B):
    global dist
    dist = abs(A[0]-B[0]) + abs(A[1]-B[1])

# 조합 구현, 총 치킨 집 중 M개 선택하는 리스트
def combs_ft(cnt, idx):
    global combs
    if cnt == M:
        combs.append(comb[:])
        return

    for i in range(idx, len(chicken)):
        comb.append(chicken[i])
        combs_ft(cnt+1, i+1)
        comb.pop()


# input
N, M = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(N)]

# 치킨집, 집 위치 찾기
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if city_map[i][j] == 2:
            chicken.append([i,j])
        elif city_map[i][j] == 1:
            house.append([i,j])

comb = []
combs = []
combs_ft(0,0)

min_dist1 = 1e9      
for comb in combs:
    all_min_dist = 0                        # 각 집에서 가장 가까운 치킨집까지 거리의 합
    for h in house:
        min_dist = 1e9
        for i in comb:
            dist = 0
            dist_ft(h,i)
            min_dist = min(dist, min_dist)      # 각 집에서 모든 치킨집까지 거리를 비교해서 가장 가까운 치킨집까지 거리를 찾음
        all_min_dist += min_dist
    min_dist1 = min(min_dist1, all_min_dist)
    
print(min_dist1)
=======
# 21:34~24:00 (2h 30m)
import itertools
import copy
from collections import deque

# input
N, M = map(int,input().split())
city_map = [list(map(int, input().split())) for _ in range(N)]

pos_chicken = []    # 치킨집 위치

for i in range(N):
    for j in range(N):
        if city_map[i][j] == 2:
            pos_chicken.append([i,j])
            

# 치킨집 위치 중 M개 선택
combs = list(itertools.combinations(pos_chicken,M))

min_dist = 1e9
# 각 조합에 대해서 해당 위치만 2로 남겨두고 나머지 2는 0으로 변환
for comb in combs:
    city_map_copy = copy.deepcopy(city_map)
    for i in range(N):
        for j in range(N):
            if city_map_copy[i][j] == 2 and [i,j] not in comb:
                city_map_copy[i][j] = 0 
    
    # bfs 구현
    q = deque()
    chicken_dist = 0
    visited = [[0]*N for _ in range(N)]
    for i in comb:
        q.append(i)
    
    while q:
        cur_pos = q.popleft()
        
        for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx, ny = cur_pos[0]+dx, cur_pos[1]+dy
            if 0>nx or nx>=N or 0>ny or ny>=N or visited[nx][ny] == 1:
                continue
            else:
                q.append([nx,ny])
                # 치킨집에서 인접한 집
                if city_map_copy[cur_pos[0]][cur_pos[1]] == 2 and city_map[nx][ny] == 1:
                    chicken_dist += 1
                    visited[nx][ny] = 1
                # 치킨집에서 인접하지는 않았지만, 집이 있는 경우
                elif city_map_copy[cur_pos[0]][cur_pos[1]] != 2 and city_map[nx][ny] == 1:
                    city_map_copy[nx][ny] = city_map_copy[cur_pos[0]][cur_pos[1]] + 1
                    chicken_dist += city_map_copy[nx][ny]
                    visited[nx][ny] = 1
                # 집이 아닌 경우 다음 경로를 위해 계속 진행
                else:
                    city_map_copy[nx][ny] = city_map[cur_pos[0]][cur_pos[1]] + 1
                    visited[nx][ny] = 1
    
    min_dist = min(chicken_dist, min_dist)
print(min_dist)               


>>>>>>> Stashed changes
