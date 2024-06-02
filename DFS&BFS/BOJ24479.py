import sys
sys.setrecursionlimit(100000)

n,m,r = map(int, input().split())

graph = [ [] for i in range(n+1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().rsplit())
    graph[a].append(b)
    graph[b].append(a)

for nodes in graph: nodes.sort()

visited = [0] * (n+1)
order = 1

def dfs(n):
    global order

    visited[n] = order
    order += 1
    for now in graph[n]:
        if not visited[now] :
            dfs(now)
dfs(r)

for i in range(1,n+1): print(visited[i])

