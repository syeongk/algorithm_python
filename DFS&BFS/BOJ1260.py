import sys
from collections import deque
n, m, v = map(int, input().split())

## 그래프 생성
unsorted_graph = [ [] for i in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    unsorted_graph[a] += [b]
    unsorted_graph[b] += [a]

## ** 2차원 리스트 내부에 있는 리스트 원소들 정렬  ex) [[5,1],[4,2]] -> [[1,5],[2,4]]
graph = [ sorted(sub_graph) for sub_graph in unsorted_graph ]

visited = [False] * (n+1)

queue = deque([v])
visited[v] = True
result_bfs = []
## bfs
while queue:
    now = queue.popleft()
    result_bfs.append(now)
    for next in graph[now]:
        if not visited[next]:
            queue.append(next)
            visited[next] = True

visited = [False] * (n+1)
result_dfs = []
def dfs(v, visited, result_dfs, graph):
    visited[v] = True
    result_dfs.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited, result_dfs, graph)

dfs(v, visited, result_dfs, graph)


print(" ".join(map(str, result_dfs)))
print(" ".join(map(str, result_bfs)))
