"""

graph 생성 - 인접리스트
방문배열 생성

"""

from collections import deque

n, m, r= map(int, input().split())

graph = [ [] for i in range(n+1)]

# g[a] += [b] 대신 append(b) 사용
for i in range(m):
    a,b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

visited = [0] * (n+1)
visited[r] = 1
queue = deque([r])
num = 1

while queue:
    now = queue.popleft()
    # 미리 내림차순 정렬
    for node in sorted(graph[now],reverse=True):
        if not visited[node]:
            num += 1
            visited[node] = num
            queue.append(node)

for i in range(1, n+1):
    print(visited[i])

