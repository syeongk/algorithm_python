from collections import deque
import sys

# n,m 을 공백으로 구분하여 입력받기
n,m = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = [ list(map(int, sys.stdin.readline().rstrip())) for i in range(n)]

# 이동할 네 방향 정의 (상,하,좌,우)
dr = [-1,1,0,0]
dc = [0,0,-1,1]

# BFS 코드 구현
def bfs(r,c):
    # 큐 구현을 위한 deque 라이브러리 사용
    queue = deque()
    queue.append((r,c))
    # 큐가 빌때까지 반복
    while queue:
        r,c = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 미로찾기 공간을 벗어난 경우 무시
            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue
            # 벽인 경우 무시
            if graph[nr][nc] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nr][nc] == 1:
                graph[nr][nc] = graph[r][c] + 1
                queue.append((nr,nc))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return graph[n-1][m-1]


# BFS 결과 출력
print(bfs(0,0))