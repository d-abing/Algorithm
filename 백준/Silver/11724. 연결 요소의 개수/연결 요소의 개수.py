import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

count = 0


def dfs(v):
    visited[v] = True
    for num in graph[v]:
        if not visited[num]:
            dfs(num)


for i in range(1, N + 1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
