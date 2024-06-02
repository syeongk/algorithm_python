import sys
sys.setrecursionlimit(100000)

n, m, r = map(int, input().split())

graph = [ [] for i in range(n+1) ]

# 그래프 저장
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 내부 리스트 내림차순 정렬
for i in graph : i.sort(reverse=True)


visited = [0] * (n+1)
order = 1

def dfs(v):
    global order

    if visited[v] == 0:
        visited[v] = order
        order += 1
        for now in graph[v]:
            dfs(now)

dfs(r)

for j in range(n):
    print(visited[j+1])
