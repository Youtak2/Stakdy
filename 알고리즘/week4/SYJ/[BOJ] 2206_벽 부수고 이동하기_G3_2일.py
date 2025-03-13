# 벽 부수고 이동하기
# 17:07~

from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

visited = [[[0,0] for _ in range(m)] for _ in range(n)]
q = deque()
    
def bfs(r,c):
    q.append([r,c,0])
    visited[r][c][0] = 1

    while q:
        r, c, break_cnt = q.popleft()

        if r == n-1 and c == m-1:
            return visited[r][c][break_cnt]
        
        for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
            nr, nc = r+dr, c+dc

            if 0<=nr<n and 0<=nc<m:

                if board[nr][nc] == 1 and break_cnt == 0:
                    visited[nr][nc][1] = visited[r][c][0] + 1
                    q.append([nr,nc,1])

                elif board[nr][nc] == 0 and visited[nr][nc][break_cnt] == 0:
                    visited[nr][nc][break_cnt] = visited[r][c][break_cnt] + 1
                    q.append([nr,nc,break_cnt])

    return -1

print(bfs(0,0))
'''
(0,0) -> (n-1, m-1)로 이동
최단 경로, 시작 칸, 끝나는 칸 포함
벽은 한 개까지 부숴도 됨
상,하,좌,우로 이동 가능

출력
최단거리, 불가능하면 -1 출력

0,0 에서 시작해서 bfs 탐색
- 0을 따라서 가기

- index를 하나 추가해서 벽을 부순 횟수 count
    - 이미 벽을 부쉈으면 0인 것만 따라가기
    - 벽을 아직 부수지 않았다면 0,1 모두 이동 가능

    - 인덱스 범위가 초과하면 break
    - 더이상 이동할 수 없으면 break
    - 인덱스가 n-1, m-1이면 종료

- 변수: n, m, board, cnt
'''
# from collections import deque

# n, m = map(int, input().split())
# board = [list(map(int, input().strip())) for _ in range(n)]

# visited = [[[0,0] for _ in range(m)] for _ in range(n)]
# visited[0][0][0] = 1

# q = deque()
# q.append([0,0,0])   # i, j, break_cnt

# while q:
#     r, c, break_cnt = q.popleft()
    
#     # if r == n-1 and c == m-1:
#     #     continue
    
#     for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:
#         nr, nc = r + dr, c + dc
#         if 0<=nr<n and 0<=nc<m:

#             # 이동 불가하고, break_cnt == 0
#             if board[nr][nc] == 1 and break_cnt == 0:
#                 visited[nr][nc][1] = visited[r][c][0] + 1
#                 q.append([nr,nc,1])
            
#             # 이동 가능할 때
#             if board[nr][nc] == 0 and visited[nr][nc][break_cnt] == 0:
#                 visited[nr][nc][break_cnt] = visited[r][c][break_cnt] + 1
#                 q.append([nr,nc,break_cnt])

# ans = visited[n-1][m-1][break_cnt]
# if ans != 0:
#     print(ans)
# else:
#     print(-1)
    



#         if nr<0 or nr>=n or nc<0 or nc>=m:
#         # or visited[nr][nc] != max_visited:  # out of index, already visited
#             continue
#         elif nr == n-1 and nc == m-1:
#             visited0[nr][nc] = visited0[r][c]+1
#             visited1[nr][nc] = visited1[r][c]+1
#             break

#         # 벽을 이미 부쉈고 가야할 곳이 벽일 때
#         if board[nr][nc] == 1 and cnt == 1:
#             continue
#         # 벽을 부수기 전이고, 가야할 곳이 벽일 때
#         elif board[nr][nc] == 1 and cnt == 0 and visited1[nr][nc] == max_visited:
#             q.append([nr,nc,1])
#             visited1[nr][nc] = min(visited0[r][c] + 1, visited1[nr][nc])
#             # min(visited[r][c] + 1, visited[nr][nc])
        
#         # 벽을 부수기 전이고, 가야할 곳이 벽이 아닐 때
#         elif board[nr][nc] == 0 and cnt == 0 and visited0[nr][nc] == max_visited:
#             q.append([nr,nc,0])
#             visited0[nr][nc] = min(visited0[r][c] + 1, visited0[nr][nc])
#             # min(visited[r][c] + 1, visited[nr][nc])
#         # 벽을 이미 부쉈고, 가야할 곳이 벽이 아닐 때
#         elif board[nr][nc] == 0 and cnt == 1 and visited1[nr][nc] == max_visited:
#             q.append([nr,nc,1])
#             visited1[nr][nc] = min(visited1[r][c] + 1, visited1[nr][nc])
#             # min(visited[r][c] + 1, visited[nr][nc])
        
# for i in visited0:
#     print(i)
# print()

# for i in visited1:
#     print(i)
# print()
# # print(cnt)
# # print(max_visited)
# # print(visited[n-1][m-1])

# # # 미로를 탈출하지 못했을 때
# # if visited[n-1][m-1] == max_visited:
# #     ans = -1
# # # 미로를 탈출한 경우
# # else:
# #     ans = visited[n-1][m-1]

# # print(ans)