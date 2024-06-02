"""

graph 생성 - 인접리스트
방문배열 생성

"""

from collections import deque

n, m, r= map(int, input().split())

g = [ [] for i in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# 미리 내림차순 정렬
for sub in g: sub.sort(reverse=True)

visited = [0] * (n+1)
visited[r] = 1
queue = deque([r])
num = 1

while queue:
    now = queue.popleft()
    for node in g[now]:
        if not visited[node]:
            num += 1
            visited[node] = num
            queue.append(node)

for i in range(1, n+1):
    print(visited[i])

