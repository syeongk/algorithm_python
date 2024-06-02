from collections import deque
import sys

# 행, 열, 미로(인접 노드 - 1) 입력받기

n, m = map(int, input().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for i in range(n)]


# 인접 노드로 탐색을 위한 이동 방향 (상,하,좌,우)
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs(r, c):
    # 큐에 시작노드 append, 시작노드 방문
    queue = deque()
    queue.append((r, c))


    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if maze[nr][nc] == 0:
                continue
            if maze[nr][nc] == 1:
                # 방문처리
                maze[nr][nc] = maze[r][c] + 1
                queue.append((nr,nc))
    return(maze[n-1][m-1])


print(bfs(0,0))

