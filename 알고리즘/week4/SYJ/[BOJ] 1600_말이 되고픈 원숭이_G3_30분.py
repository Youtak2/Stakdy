from collections import deque

k = int(input())
w, h = map(int, input().split())
board = [(list(map(int, input().split()))) for _ in range(h)]

# 0: 이동 가능, 1: 장애물
# k 번 horse 처럼 이동 가능
# (0,0)에서 (h-1, w-1)까지 이동 가능하면 횟수 출력, 불가능하면 -1 출력

def bfs(r, c, horse_cnt):
    visited = [[[0 for _ in range(k+1)] for _ in range(w)] for _ in range(h)]
    q = deque()

    q.append([r, c, horse_cnt])

    while q:
        r, c, horse_cnt = q.popleft()
        if r == h-1 and c == w-1:
            return visited[r][c][horse_cnt]

        for hr, hc in [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]:
            nr, nc = r + hr, c + hc

            if 0<=nr<h and 0<=nc<w and horse_cnt < k and visited[nr][nc][horse_cnt+1] == 0 and board[nr][nc] == 0:
                    visited[nr][nc][horse_cnt+1] = visited[r][c][horse_cnt] + 1
                    q.append([nr,nc,horse_cnt+1])

        for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
            nr, nc = r + dr, c + dc

            if 0<=nr<h and 0<=nc<w and visited[nr][nc][horse_cnt] == 0 and board[nr][nc] == 0:
                visited[nr][nc][horse_cnt] = visited[r][c][horse_cnt] + 1
                q.append([nr,nc,horse_cnt])
        
    return -1

print(bfs(0,0,0))


'''
horse처럼 이동하는 것 정의
hr = 
hc =

bfs 함수로 구현
    visited = [[0 *k ] *m] *h
    0 index = 인접 방향으로 이동
    1 index = horse로 1번
    2 index = horse로 2번 ...

    q.append([r, c, horse_cnt])

    while q:
    
    nr, nc : index 범위 내에 있을 때, visited[nr][nc][horse_cnt] == 0

        horse 처럼 이동 한 곳이 장애물이 아닐 때 & horse_cnt < k
            horse로 이동
            visited += 1
            q.append(nr, nc, horse_cnt+1)

        horse 처럼 이동한 곳이 장애물 or horse_cnt == k
            인접 한 곳으로 이동 가능한 경우
                인접 한 곳으로 이동
                visited += 1
                q.append(nr, nc, horse_cnt)
    

    
'''