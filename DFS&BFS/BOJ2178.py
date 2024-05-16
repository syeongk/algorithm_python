from collections import deque
import sys

# 행, 열 입력받기
n, m = map(int, input().split())


def BFS(x,y):
    maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

    start = maze[0][0]
    queue_now = deque([start])
    count = 1

    # queue_now가 비어있으면 False로 간주
    while queue_now:
        # 큐의 left의 인접노드 (범위 넘어가지 않고 1인 노드만) 큐에 추가. 추가한 인접노드를 배열에서 최단경로 값으로 변경한다.
        node = queue_now.popleft()

        direction = [maze[x-1][y], maze[x][y-1], maze[x+1][y], maze[x][y+1]]
        for i in direction:
            if i == 1 and i != None:
                queue_now.append()
                count += 1
                i = count

    return maze[n][m]


print(BFS(n,m))
