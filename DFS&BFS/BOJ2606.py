'''
vertex 개수
edge 개수

Graph 생성 [ [],[],[],[],[],[],[],[] ]  리스트 컴프리헨션, vertex + 1 개
인접 리스트 [ [],[2,5],[3],[],[7],[2,6],[],[] ]  for문, append

visited = [-1]* n+1
count = 0

queue 생성, 시작노드 1
while 큐가 빔:
 now = pop
 for next graph[now]
  if 방문X
   count++
   append

'''
from collections import deque

v = int(input())
e = int(input())
count = 0

graph = [ [] for i in range(v+1)]

for i in range(e):
    a, b = map(int, input().split())
    graph[a] = graph[a] + [b]
    graph[b] = graph[b] + [a]

visited = [False] * (v+1)


queue = deque([1])
visited[1] = True
while queue:
    now = queue.popleft()
    for next in graph[now]:
        if visited[next] == False:
            visited[next] = True
            queue.append(next)
            count += 1

print(count)